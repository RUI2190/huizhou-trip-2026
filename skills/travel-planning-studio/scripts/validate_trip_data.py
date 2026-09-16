#!/usr/bin/env python3
"""Validate the canonical JSON shared by a trip guide, map, and PDF."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


COORDINATE_SYSTEMS = {"wgs84", "gcj02", "bd09"}
STATUSES = {"booked", "confirmed", "candidate", "backup", "needs_recheck"}
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", type=Path, help="Path to trip-data.json")
    return parser.parse_args()


def is_iso_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def is_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def require_text(obj: dict, key: str, path: str, report: Report) -> None:
    if not isinstance(obj.get(key), str) or not obj[key].strip():
        report.error(f"{path}.{key} must be a non-empty string")


def validate_source(source: object, path: str, report: Report) -> None:
    if not isinstance(source, dict):
        report.error(f"{path} must be an object")
        return
    if not is_http_url(source.get("url")):
        report.error(f"{path}.url must be a valid HTTP(S) URL")
    if not is_iso_date(source.get("checked_at")):
        report.error(f"{path}.checked_at must be an ISO date (YYYY-MM-DD)")
    claims = source.get("claims")
    if not isinstance(claims, list) or not claims or not all(
        isinstance(claim, str) and claim.strip() for claim in claims
    ):
        report.error(f"{path}.claims must be a non-empty list of strings")
    confidence = source.get("confidence")
    if confidence is not None and confidence not in {"high", "medium", "low"}:
        report.error(f"{path}.confidence must be high, medium, or low")


def validate_poi(poi: object, index: int, report: Report) -> str | None:
    path = f"pois[{index}]"
    if not isinstance(poi, dict):
        report.error(f"{path} must be an object")
        return None

    for key in ("id", "name", "category", "address"):
        require_text(poi, key, path, report)

    poi_id = poi.get("id")
    if isinstance(poi_id, str) and not ID_PATTERN.fullmatch(poi_id):
        report.error(f"{path}.id must use lowercase letters, numbers, hyphens, or underscores")

    status = poi.get("status")
    if status not in STATUSES:
        report.error(f"{path}.status must be one of {sorted(STATUSES)}")

    coordinate_system = poi.get("coordinate_system")
    if coordinate_system not in COORDINATE_SYSTEMS:
        report.error(
            f"{path}.coordinate_system must be one of {sorted(COORDINATE_SYSTEMS)}"
        )

    lat = poi.get("lat")
    lon = poi.get("lon")
    if not isinstance(lat, (int, float)) or isinstance(lat, bool) or not -90 <= lat <= 90:
        report.error(f"{path}.lat must be a number from -90 to 90")
    if not isinstance(lon, (int, float)) or isinstance(lon, bool) or not -180 <= lon <= 180:
        report.error(f"{path}.lon must be a number from -180 to 180")

    sources = poi.get("sources")
    if not isinstance(sources, list) or not sources:
        report.error(f"{path}.sources must be a non-empty list")
    else:
        for source_index, source in enumerate(sources):
            validate_source(source, f"{path}.sources[{source_index}]", report)

    return poi_id if isinstance(poi_id, str) else None


def validate_trip(trip: object, report: Report) -> None:
    if not isinstance(trip, dict):
        report.error("trip must be an object")
        return
    for key in ("destination", "timezone"):
        require_text(trip, key, "trip", report)
        if trip.get(key) == "REPLACE_ME":
            report.error(f"trip.{key} still contains the scaffold placeholder REPLACE_ME")
    for key in ("start_date", "end_date"):
        if key in trip and trip[key] not in (None, "") and not is_iso_date(trip[key]):
            report.error(f"trip.{key} must be an ISO date (YYYY-MM-DD)")
    start = trip.get("start_date")
    end = trip.get("end_date")
    if is_iso_date(start) and is_iso_date(end) and start > end:
        report.error("trip.start_date must not be after trip.end_date")


def validate_days(days: object, poi_ids: set[str], report: Report) -> int:
    if not isinstance(days, list):
        report.error("days must be a list")
        return 0
    day_ids: list[str] = []
    for index, day in enumerate(days):
        path = f"days[{index}]"
        if not isinstance(day, dict):
            report.error(f"{path} must be an object")
            continue
        for key in ("id", "title"):
            require_text(day, key, path, report)
        if isinstance(day.get("id"), str):
            day_ids.append(day["id"])
        if not is_iso_date(day.get("date")):
            report.error(f"{path}.date must be an ISO date (YYYY-MM-DD)")
        stops = day.get("stops")
        if not isinstance(stops, list):
            report.error(f"{path}.stops must be a list")
            continue
        for stop_index, stop in enumerate(stops):
            stop_path = f"{path}.stops[{stop_index}]"
            if not isinstance(stop, dict):
                report.error(f"{stop_path} must be an object")
                continue
            poi_id = stop.get("poi_id")
            if not isinstance(poi_id, str) or not poi_id:
                report.error(f"{stop_path}.poi_id must be a non-empty string")
            elif poi_id not in poi_ids:
                report.error(f"{stop_path}.poi_id references unknown POI: {poi_id}")

    duplicates = [item for item, count in Counter(day_ids).items() if count > 1]
    for duplicate in duplicates:
        report.error(f"duplicate day id: {duplicate}")
    return len(days)


def validate(data: object) -> tuple[Report, int, int]:
    report = Report()
    if not isinstance(data, dict):
        report.error("top-level JSON value must be an object")
        return report, 0, 0

    validate_trip(data.get("trip"), report)

    pois = data.get("pois")
    poi_ids_list: list[str] = []
    names: list[str] = []
    coordinates: list[tuple[float, float, str]] = []
    if not isinstance(pois, list):
        report.error("pois must be a list")
        pois = []
    for index, poi in enumerate(pois):
        poi_id = validate_poi(poi, index, report)
        if poi_id:
            poi_ids_list.append(poi_id)
        if isinstance(poi, dict):
            if isinstance(poi.get("name"), str):
                names.append(re.sub(r"\s+", "", poi["name"]).casefold())
            lat, lon, system = poi.get("lat"), poi.get("lon"), poi.get("coordinate_system")
            if isinstance(lat, (int, float)) and isinstance(lon, (int, float)) and isinstance(system, str):
                coordinates.append((round(float(lat), 6), round(float(lon), 6), system))

    for duplicate in (item for item, count in Counter(poi_ids_list).items() if count > 1):
        report.error(f"duplicate POI id: {duplicate}")
    for duplicate in (item for item, count in Counter(names).items() if item and count > 1):
        report.warn(f"possible duplicate POI name: {duplicate}")
    for duplicate in (item for item, count in Counter(coordinates).items() if count > 1):
        report.warn(f"multiple POIs share coordinates: {duplicate}")

    day_count = validate_days(data.get("days", []), set(poi_ids_list), report)
    if not pois:
        report.warn("no POIs are present yet")
    if day_count == 0:
        report.warn("no itinerary days are present yet")
    return report, len(pois), day_count


def main() -> int:
    args = parse_args()
    try:
        with args.json_file.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.json_file}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")
        return 1

    report, poi_count, day_count = validate(data)
    for message in report.errors:
        print(f"ERROR: {message}")
    for message in report.warnings:
        print(f"WARNING: {message}")
    print(
        f"Validated {poi_count} POI(s) and {day_count} day(s): "
        f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)."
    )
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

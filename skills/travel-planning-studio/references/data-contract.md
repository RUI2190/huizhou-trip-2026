# Canonical data contract

The canonical JSON is the shared source for the itinerary, map, and PDF. Keep presentation-specific text outside it unless the text is reused across deliverables.

## Top-level fields

- `trip`: destination, timezone, travel dates, traveler groups, arrival and departure segments, and generation metadata.
- `pois`: normalized places, transport nodes, lodging, food, shops, and activities.
- `days`: ordered itinerary days containing references to POI IDs.
- `assumptions`: important defaults or unknowns that influence the plan.
- `decisions`: selected options and material corrections that define the current baseline.
- `branches`: unresolved itinerary alternatives with triggers and decision deadlines.
- `rechecks`: time-sensitive facts with an owner, due date or trigger, and consequence.

See `assets/example-trip-data.json` for a minimal valid example.

## POI fields

Required fields:

- `id`: stable lowercase identifier using letters, numbers, hyphens, or underscores;
- `name`, `category`, `address`;
- `lat`, `lon`, and `coordinate_system` (`wgs84`, `gcj02`, or `bd09`);
- `status` (`booked`, `confirmed`, `candidate`, `backup`, or `needs_recheck`);
- `sources`: at least one evidence object.

Recommended fields include `area`, `reason`, `day_ids`, `opening_notes`, `reservation_notes`, `cost_notes`, `accessibility_notes`, `weather_notes`, `coordinate_precision`, and provider-specific navigation identifiers.

Each source object contains:

- `url`: the underlying HTTP or HTTPS page;
- `checked_at`: ISO date such as `2026-09-16`;
- `claims`: one or more short claims supported by that page;
- optional `confidence`: `high`, `medium`, or `low`.

## Day fields

Each day needs a unique `id`, ISO `date`, title, and ordered `stops`. Every stop must reference an existing POI with `poi_id`. Optional stop fields include `window`, `duration_minutes`, `transfer_minutes`, `optional`, and `notes`.

Keep fallbacks in a day-level `fallbacks` array or as backup POIs. Do not duplicate the full POI object inside a day.

For separately arriving travelers, store distinct arrival segments instead of averaging their times. A branch may reference shared days, but it should only duplicate the stops that actually differ.

## Validation

Run:

```bash
python3 scripts/validate_trip_data.py path/to/trip-data.json
```

Errors block generation. Warnings identify likely quality problems that require review but may be intentional.

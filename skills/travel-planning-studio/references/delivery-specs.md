# Delivery specifications

Read only the sections needed for the requested deliverables.

## Assign jobs before formats

Decide what each artifact is for. A useful default for a full package is:

- the PDF or written guide is the pre-trip plan and offline reference;
- the interactive map is the travel-day location, nearby-discovery, and navigation handoff tool;
- the canonical dataset is the maintained source of truth.

Avoid copying the same long narrative into every artifact. Put context and decision rationale in the guide; put current location, nearby POIs, concise notes, copy actions, and navigation in the map.

## Written travel guide

Lead with decisions the traveler will use: trip shape, bookings, daily plan, reservations, and recheck list. Keep background narrative subordinate to actionability.

Recommended sections:

1. trip summary and assumptions;
2. booked items and critical constraints;
3. day-by-day itinerary;
4. food, cafes, shopping, and backups by area;
5. transportation and navigation notes;
6. reservations, tickets, and pre-departure rechecks;
7. source notes where precision matters.

## Interactive map

Build mobile-first and derive all POIs from the canonical dataset.

Required behavior for a full package:

- category filters whose colors match markers;
- search by name, area, category, and address;
- tap a marker to open details without unexpected map movement;
- copy name and address;
- links to locally relevant navigation providers;
- optional multi-stop route planning with explicit travel modes;
- route-stop overlays that do not block the underlying POI marker;
- reusable user-location marker rather than stacked markers;
- expandable notes for coordinate uncertainty and map data sources;
- compact controls that do not overlap at common phone widths.
- travel-useful access and service points when verified, such as entrances, drop-off points, parking, stations, rental return, toilets, or luggage storage;
- essential POI text that remains available when tiles or routing fail.

Network and coordinate requirements:

- self-host critical client libraries when the target network may not reach a public CDN;
- choose a tile provider reachable in the deployment region and provide a fallback when practical;
- keep data coordinates labeled and transform only at map, routing, or navigation boundaries;
- test a known landmark at high zoom for alignment;
- retain provider attribution and comply with provider terms;
- do not expose API secrets in client-side code.
- deploy over HTTPS when browser geolocation is required;
- show clear map, routing, and location failure states rather than a blank surface.

## PDF guide

The PDF must be usable offline and readable on both phone and A4 or Letter output.

- Use a clear cover or title block, table of contents only when length warrants it, and strong day-level hierarchy.
- Prefer tables for bookings, transportation, and recheck items; prefer prose for rationale and local context.
- Keep addresses, phone numbers, reservation notes, and map links selectable.
- Include short URLs or QR codes only when they materially help; keep the written destination or address as a fallback.
- Do not rely on color alone to encode categories.
- Include a compact relative-location overview or schematic map when it materially helps the reader understand the trip shape.
- Use decision tables for open branches or mode choices when the tradeoffs matter.
- Render every page to images and inspect clipping, orphan headings, unreadable tables, missing glyphs, and link overflow before delivery.
- If the PDF and website differ in freshness, state which is canonical and when each was generated.

## Naming and versioning

Use stable names such as:

- `YYYY-MM-DD_destination_travel-guide.pdf`
- `destination-trip-map/`
- `trip-data.json`

Keep “draft,” “client-review,” and “final” in metadata or release notes when possible. Avoid chains such as `final-v3-revised-final`.

## Canonical synchronization

Generate repeated facts—names, dates, addresses, coordinates, status, and day assignments—from the same data source. A manual change in only the PDF or only the map is a synchronization defect.

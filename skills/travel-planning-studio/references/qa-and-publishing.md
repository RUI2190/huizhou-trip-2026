# QA and publishing

Use this reference before final delivery or whenever an existing package is audited.

## Data and editorial QA

- Validate the canonical JSON with `scripts/validate_trip_data.py`.
- Confirm every itinerary POI exists in the dataset.
- Check duplicates, category consistency, coordinate ranges, coordinate systems, and source dates.
- Compare booked items against the user's source material.
- Mark unsupported or stale claims for recheck.
- Verify the guide, map, and PDF use the same names, dates, and statuses.

## Map QA

Test the deployed page, not only a local file.

- phone and desktop breakpoints;
- tile and client-library loading on the target network;
- essential POI information and error messaging under a failed or degraded tile connection;
- marker alignment at a known landmark;
- category on or off behavior and intended recentering rules;
- search results and clear or dismiss behavior;
- POI detail, copy address, and copy name;
- user location, including permission denial and repeated clicks;
- geolocation from the final HTTPS URL and not only from localhost;
- route add, remove, reorder, clear, travel-mode switching, and real path rendering;
- route-number markers do not intercept POI clicks;
- external navigation URLs use the correct provider coordinate system;
- controls, attribution, bottom sheets, and route panels do not overlap;
- console errors and failed network requests.
- home-screen or PWA behavior when that feature is included.

If a provider cannot support a travel mode or region, explain the fallback instead of simulating a route.

## PDF QA

- render all pages and inspect them visually;
- verify fonts and CJK glyphs;
- inspect headings, tables, page breaks, images, and margins;
- test links and QR codes where included;
- ensure no private booking code or personal identifier appears unintentionally;
- compare a sample of dates, addresses, and prices against the canonical dataset.

## Publication workflow

1. Run local checks and review the exact diff.
2. Preserve unrelated user changes and repository history.
3. Stage the final artifacts and use a concise commit message.
4. Obtain required action-time confirmation before a public commit or upload.
5. Wait for deployment completion rather than assuming a successful commit means a live site.
6. Open the final public URL with a cache-busting query when necessary.
7. Repeat the critical mobile and routing checks online.
8. Return the clean public URL, commit or release identifier, and a concise QA summary.

## Completion report

Report:

- delivered artifacts and links;
- important assumptions and defaults;
- validation performed and observed results;
- facts or reservations that still need rechecking;
- known provider, network, or data limitations.

Do not describe a feature as tested when only its source code was inspected.

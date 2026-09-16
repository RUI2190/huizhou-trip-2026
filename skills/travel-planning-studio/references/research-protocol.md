# Research protocol

Use this reference whenever current facts, recommendations, prices, schedules, regulations, or precise source attribution matter.

## Research sequence

1. Translate the brief into a query matrix: destination, dates, transport, lodging, attractions, food, cafes, shopping, events, practicalities, and risk items.
2. Start with first-party sources: official attraction, museum, railway, airline, transit, tourism authority, hotel, restaurant, or government pages.
3. Use reputable secondary sources for discovery and lived-experience signals, not as the sole authority for critical facts.
4. Cross-check facts that can derail a day: closure day, last admission, reservation requirement, transfer duration, seasonal access, holiday schedule, and exact location.
5. Record the source URL, checked date, supported claim, and confidence in the source log.

State material access limitations. If a platform, private post, paywall, app-only result, or search index could not be inspected adequately, do not imply that it was exhaustively researched.

## Evidence hierarchy

Prefer, in order:

1. official operator or government source;
2. official booking or ticket channel;
3. major mapping or transportation platform;
4. established travel publication or local reporting;
5. recent review platforms and social posts for qualitative signals only.

Do not let popularity rankings substitute for fit. Evaluate each candidate against the party, pace, geography, time window, and budget.

## Freshness and claim handling

- Treat hours, prices, schedules, entry rules, personnel, closures, and holiday operations as time-sensitive.
- Store `checked_at` for each supporting source.
- Write “typical,” “currently listed,” or “recheck before departure” when a fact is not guaranteed for the travel date.
- Preserve disagreements between sources instead of silently choosing the most convenient value.
- Never cite a search-result snippet when the underlying page is available.
- Separate facts that can be verified now from facts that only become reliable near departure, and assign the latter a recheck date or trigger.

## POI normalization

Each POI should have:

- stable `id`, display name, category, and area;
- address plus latitude and longitude;
- explicit `coordinate_system`;
- status and suitable day or time window;
- concise reason for inclusion;
- known reservation, opening, cost, accessibility, or weather notes;
- one or more sources with checked dates and supported claims.

Deduplicate aliases and branches. Keep approximate coordinates labeled as approximate; navigation should favor a verified address or provider search when precision is uncertain.

## Coordinate discipline

- Determine whether source coordinates are `wgs84`, `gcj02`, or `bd09` before transforming.
- Chinese mapping platforms commonly expose shifted domestic coordinates; do not apply the same transform twice.
- Use WGS-84 for global routing services and providers that expect it.
- Use GCJ-02 for AMap-style domestic basemaps and navigation.
- Verify alignment at high zoom on at least one known landmark before applying a conversion to the full dataset.

## Recommendation scoring

Score candidates internally across:

- user fit;
- geographic efficiency;
- evidence quality and freshness;
- uniqueness or local relevance;
- time and weather resilience;
- reservation or queue risk;
- accessibility and budget fit.

Expose the rationale, not fake numeric precision, unless the user asks for a scoring table.

# Intake and defaults

Use this reference for a new trip or when the scope changes materially.

## Input tiers

### Minimum viable input

Obtain or infer from existing context:

- destination or destination range;
- date window or trip length;
- traveler count and broad party type;
- starting point and required end point when routing depends on them.

If even the destination or travel window is unknown, ask one consolidated question before researching. A user may explicitly request an inspiration-first proposal; in that case treat destination and dates as variables and provide options rather than pretending they are fixed.

### High-impact personalization

Ask only when missing information would substantially change the plan:

- confirmed transport and accommodation, including arrival and departure times;
- walking tolerance, driving eligibility, mobility or accessibility constraints;
- children, older travelers, pregnancy, or other pace considerations the user chooses to disclose;
- dietary requirements and allergies;
- budget band and whether it applies per person or to the group;
- must-do, must-eat, must-avoid, shopping, nightlife, photography, or rest priorities;
- preference for public transit, taxi or ride-hailing, self-drive, cycling, or walking;
- desired output language, map provider, PDF, website, and publishing destination.

### Useful but non-blocking

- room style, restaurant atmosphere, preferred wake and sleep times;
- tolerance for queues, weather exposure, early starts, or spontaneous changes;
- luggage constraints, charging needs, data roaming, payment methods;
- visual style and brand preferences for deliverables.

## Defaults when the user says to proceed

Use these only for missing non-critical choices and disclose them:

- moderate pace with one anchor experience per half-day;
- a balanced mix of signature sights and locally specific experiences;
- mid-range spending, with clearly labeled lower-cost and higher-cost alternatives;
- walking plus public transit or taxi, whichever is locally realistic;
- 15–30 minute urban transfer buffers and larger buffers for intercity moves;
- one meal candidate and one backup near each major activity cluster;
- mobile-first map, concise guide, and readable PDF typography;
- no public exposure of personal or booking details.

Do not interpret silence as “no allergies,” “no accessibility needs,” or “eligible for entry.” State that these inputs were not provided.

## One-pass intake format

Prefer a single compact request grouped by impact:

1. Dates, party, arrival, departure, and fixed bookings.
2. Pace, mobility, diet, budget, and transport constraints.
3. Must-do and must-avoid preferences.
4. Requested deliverables and whether public hosting is wanted.

Do not ask the user to supply information that can be researched safely, such as typical opening hours, attraction locations, neighborhood clustering, or available public transportation modes.

## Constraint model

Record each item as one of:

- `hard`: cannot be violated;
- `strong`: violate only with an explicit tradeoff;
- `flexible`: optimize when convenient;
- `unknown`: requires a stated assumption or later recheck;
- `booked`: externally committed and treated as hard unless the user asks to change it.

This model prevents a casual preference from displacing a paid booking or safety constraint.

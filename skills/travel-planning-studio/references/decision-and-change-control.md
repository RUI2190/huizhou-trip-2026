# Decision and change control

Use this reference when the user has not selected a trip shape, travelers arrive separately, dates have open branches, or confirmed details change during planning.

## Compare trip shapes before optimizing details

When there are genuinely different ways to structure the trip, create a small set of distinct options rather than superficial variations. Compare each option on:

- hotel changes and luggage burden;
- geographic efficiency and travel time;
- pace, crowd exposure, and weather resilience;
- access to the user's highest priorities;
- estimated budget range and the largest price uncertainties;
- what the user gains and gives up.

Recommend one option with a clear reason, retain meaningful alternatives, and stop expanding the option set once each remaining option serves a distinct preference. Do not research every restaurant and POI deeply until the trip shape is selected.

## Lock the execution baseline

After the user chooses an option, restate the execution baseline: dates, traveler groups, booked lodging and transport, fixed appointments, open decisions, and requested deliverables. Mark superseded assumptions so they are not carried into later outputs.

Treat user wording about a booking as provisional until the exact property, branch, date, occupancy, and address can be matched to the booking evidence. If public sources suggest a spelling correction or similarly named venue, flag the discrepancy rather than silently replacing the user's booking.

## Multiple origins and rendezvous

Represent travelers arriving from different origins as separate arrival segments. Plan:

- what each traveler does before the group is complete;
- the meeting point and communication fallback;
- luggage, check-in, meal, and late-arrival handling;
- which activities require the whole group and which do not.

Do not plan the arrival day as if everyone appears at the destination simultaneously.

## Conditional branches

For unresolved choices such as an optional extra night, weather-dependent excursion, or unconfirmed train:

- give the branch a decision deadline and trigger;
- keep the shared itinerary before the branch in one place;
- describe only the days and bookings that change;
- show cancellation, ticket, transfer, and budget consequences;
- prevent a branch from being presented as confirmed.

## Change log

When the user corrects party size, accommodation, dates, or transport, update the canonical brief first. Record:

- old value and new value;
- when and why it changed;
- which days, costs, routes, POIs, or deliverables are affected;
- which generated artifacts must be refreshed.

A polished artifact based on an old party size or old hotel is still wrong. Re-run affected feasibility and consistency checks after every material change.

## Staged delivery

For a complex package, a labeled working skeleton can reduce rework when the product shape still needs feedback. Clearly separate:

- concept or feasibility version;
- execution-ready version;
- pre-departure refreshed version.

Do not label a skeleton “final,” and do not make the user re-approve details they already locked.

# Field readiness

Use this reference when a map, guide, or transport recommendation will be used during the trip rather than only for planning beforehand.

## Design for the moment of use

The traveler should be able to answer quickly:

- where am I;
- what useful verified places are nearby;
- what is the next stop and how far is it;
- which mode is realistic now;
- what is the backup if the place is closed, crowded, or unreachable.

Include access and service POIs when they improve decisions: entrances, parking or drop-off points, stations, toilets, luggage storage, charging, rental return, visitor centers, pharmacies, and safe meeting points. Do not add categories merely to make the map look rich.

## Local mobility and rental feasibility

For bicycles, scooters, motorcycles, cars, boats, or other rented mobility, check the whole operating model:

- legal eligibility, license, age, insurance, deposit, and payment;
- actual operator, opening hours, inventory uncertainty, pickup and return rules;
- helmet or safety equipment, passenger and luggage limits;
- road class, surface, gradient, traffic, lighting, weather, range or fuel, and charging;
- parking, restricted zones, breakdown support, and a return fallback;
- whether the mode saves meaningful time after setup and return.

Use a mode for the part of the trip it suits. Do not force a long rural leg merely because a rental lasts all day. Label unverified rental availability as a recheck item, not as a confirmed plan.

## Crowd intelligence

Tour products and recent traveler reports can reveal common arrival windows, dwell times, entrances, and congestion patterns. Use them to design crowd-avoidance choices, but do not assume a group-tour timetable or old social post remains current. Preserve the user's preferred wake-up time unless an early start creates a clear, material benefit.

## Weak-network behavior

For an on-trip web map:

- keep essential POI names, addresses, notes, and day assignments available even if map tiles fail;
- show an understandable tile, routing, or location error state;
- make copy and external-navigation actions usable without depending on an open detail request;
- avoid client dependencies that are inaccessible on the target network;
- use HTTPS or another secure context for browser geolocation;
- add PWA metadata or home-screen support only when it improves the requested field experience.

Do not claim full offline navigation unless tiles, routing, and location behavior were actually implemented and tested offline.

## Recheck cadence

Schedule rechecks according to when facts become knowable:

- booking window: tickets, rooms, permits, and cancellation terms;
- weeks before departure: holiday events, road works, seasonal access, and local transport;
- several days before: weather, temporary closures, rental availability, and operating notices;
- travel day: delays, live traffic, last-mile availability, and meeting instructions.

Put each unresolved item on the recheck list with an owner, trigger, and decision consequence.

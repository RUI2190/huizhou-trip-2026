---
name: travel-planning-studio
description: Research, design, produce, audit, or refresh personalized travel packages that may include an evidence-backed itinerary, POI dataset, mobile interactive map, PDF guide, and optional publication. Use for multi-part trip planning and travel deliverables; do not invoke for a single isolated travel fact or a simple booking lookup.
---

# Travel Planning Studio

Create a usable travel product, not a list of attractions. Preserve the user's hard constraints, make uncertain facts visible, and keep the itinerary, map, and PDF synchronized from one canonical dataset.

## Select the delivery mode

- **Quick itinerary:** itinerary and concise recommendations only.
- **Full travel package:** research dossier, day-by-day plan, normalized POI data, interactive map, PDF guide, and optional hosting.
- **Refresh or audit:** update time-sensitive facts, repair route or map issues, and regenerate only affected deliverables.

Do not expand a quick request into a website or PDF unless the user asks for them. If the user asks for an end-to-end package, complete all safe in-scope work without stopping for optional preferences.

## Gather only decision-changing inputs

For a new project, read [references/intake-and-defaults.md](references/intake-and-defaults.md). Consolidate truly blocking questions into one short intake. If the user has already provided enough information, proceed without asking again.

Never infer allergies, accessibility needs, visa or entry eligibility, medical requirements, exact budget limits, paid bookings, or permission to publish personal information. Missing non-critical preferences may use the documented defaults, which must be disclosed in the final handoff.

## Core workflow

1. **Frame the trip.** Separate hard constraints, strong preferences, flexible preferences, unknowns, and already-booked items. Select a delivery mode and working timezone. When the trip has competing shapes, multiple arrival groups, unresolved dates, or changing bookings, read [references/decision-and-change-control.md](references/decision-and-change-control.md).
2. **Build the evidence base.** For current travel facts, browse authoritative or first-party sources and keep a source log. Read [references/research-protocol.md](references/research-protocol.md) and apply [references/selection-frameworks.md](references/selection-frameworks.md) to lodging, food, attractions, shopping, and transport.
3. **Create one canonical dataset.** Normalize POIs, coordinates, coordinate systems, dates, evidence, and status labels before writing multiple deliverables. Read [references/data-contract.md](references/data-contract.md). Use `scripts/init_trip_project.py` for a new file-based workspace and `scripts/validate_trip_data.py` before rendering.
4. **Design the itinerary.** Cluster geographically, respect opening windows and transfers, include realistic buffers, and provide recovery options. Read [references/itinerary-logic.md](references/itinerary-logic.md).
5. **Produce requested deliverables.** Assign each artifact a travel-stage job, then derive the prose guide, map, route planner, and PDF from the same dataset. Read [references/delivery-specs.md](references/delivery-specs.md). When a PDF is requested, use available PDF or document tooling and follow its render-and-verify workflow.
6. **Verify observable behavior.** Test facts, coordinates, mobile layout, navigation links, copy actions, route calculation, offline or regional network dependencies, and the rendered PDF. For a travel-day map or uncertain local mobility, read [references/field-readiness.md](references/field-readiness.md). Use [references/qa-and-publishing.md](references/qa-and-publishing.md) for final QA and deployment.
7. **Publish only when authorized.** Prepare deployment safely, then obtain any action-time confirmation required for a public commit, upload, permission change, or share operation. Verify the public URL after deployment.

## Non-negotiable quality rules

- Label items as `booked`, `confirmed`, `candidate`, `backup`, or `needs_recheck`; do not blur these states.
- Do not fabricate opening hours, prices, reservation status, transit schedules, or precise coordinates.
- Store the checked date and supporting URL for time-sensitive claims.
- Recheck holiday hours, closures, ticket rules, transportation, and weather-sensitive activities close to departure.
- Keep map coordinates and navigation coordinates in an explicit system such as `wgs84`, `gcj02`, or `bd09`; transform only at provider boundaries.
- In mainland-China deployments, do not rely solely on services or CDNs that may be unreachable there. Self-host critical client libraries when practical and test the actual tile provider.
- Avoid overpacking. A technically possible route is not automatically a humane itinerary.
- Keep public deliverables free of unnecessary personal information, booking codes, phone numbers, or precise private locations.

## Recommended project layout

Use this only when the user wants saved artifacts or an ongoing project:

```text
trip-project/
├── trip-brief.yaml
├── data/trip-data.json
├── research/source-log.md
├── outputs/guide/
├── outputs/map/
└── outputs/pdf/
```

Name the project for destination and travel window, not for a temporary version number. Keep versions in commits or release metadata rather than duplicating near-identical folders.

## Completion standard

The task is complete when the requested deliverables agree with the canonical data, required QA has passed, uncertainties and recheck items are visible, and the user receives working artifact paths or verified public URLs. Report important defaults and known limitations succinctly.

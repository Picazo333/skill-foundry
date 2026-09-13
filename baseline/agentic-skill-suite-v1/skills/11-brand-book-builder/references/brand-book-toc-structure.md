# Reference: brand book table-of-contents structure by depth

Used in `SKILL.md` steps 2–3 (choose depth, build narrative sequence). Fixed
section order at every depth: essence → strategy snapshot → voice → visual
system → applications → governance. Depth controls which sections are
included and how much of each, never the order.

## Executive depth
For leadership sign-off, not day-to-day production use.
1. **Essence** — one-paragraph positioning + mission summary.
2. **Strategy snapshot** — positioning statement, value proposition, primary
   audience (from `BRAND_STRATEGY.md` if supplied, else derived from
   `MESSAGE_HIERARCHY.md`'s master message — never invented if neither
   supplies it).
3. **Voice snapshot** — the 3–5 principle names only (no full DO/DON'T set),
   one elevator pitch.
4. **Visual snapshot** — primary logo lockup, core color roles, primary
   typeface, one hero application example.
5. **1-page do/don't** — the single clearest DO/DON'T pair from each of
   voice and visual.

No governance section, no full asset checklist inline (still produced as a
separate file per step 7).

## Operational depth
For an in-house team executing day to day.
1. **Essence**
2. **Strategy snapshot**
3. **Voice** — full principle set with DO/DON'T, tone modulation matrix,
   vocabulary rules (preferred/avoided/prohibited), message hierarchy
   (pillars, descriptions at three lengths).
4. **Visual system** — full color roles + contrast behavior, typography
   roles/hierarchy, grid/spacing/imagery/iconography rules, referenced
   `DESIGN_TOKENS.json` values inline where a designer would need them.
5. **Applications** — paired voice + visual guidance per surface covered in
   `APPLICATION_RULES.md` (web, social, decks, documents, ads, product/UI).
6. No full governance/versioning section — a short "how to propose a change"
   pointer only.

## Full depth
For an external agency or client-facing deliverable.
Everything in Operational, plus:
7. **Governance** — versioning/ownership, exceptions and forbidden
   combinations (from `IDENTITY_SYSTEM.md`), any flagged coherence gaps from
   step 6 stated explicitly (not buried), a change-request process.
8. **Appendix** — full `DESIGN_TOKENS.json` reference table, glossary of
   prohibited claims/terms.

## Choosing depth when constraints don't specify
Default to `operational` when the audience is unstated and the source
artifacts are complete — it is the depth a real production team can act on.
Only default to `executive` when `mode: QUICK` is explicitly requested.
Escalate to `full` only when the objective/constraints name an external
audience (agency, client, investor).

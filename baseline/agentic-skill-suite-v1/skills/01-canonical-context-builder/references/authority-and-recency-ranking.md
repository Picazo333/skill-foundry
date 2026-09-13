# Reference: ranking source authority and recency

Used in `SKILL.md` step 1 (Inventory sources).

## Authority order (highest first)
1. Signed-off/delivered deliverables (shipped doc, approved brief, merged code).
2. Explicit decisions recorded as decisions (a decision log entry, a "final:" note).
3. Structured working documents (specs, briefs, canon itself if updating).
4. Direct stakeholder statements in conversation.
5. Draft/working chat asides, brainstorm notes, superseded drafts.

## Recency rule
Within the same authority tier, a later timestamp supersedes an earlier one
for the same claim — but only within the same tier. A draft chat aside from
yesterday does not outrank a signed-off deliverable from last month; it goes
to `OPEN_LOOPS.md` as a possible pending change instead of silently
overwriting canon.

## When authority and recency conflict
If a lower-authority but newer source contradicts a higher-authority but
older one, do not resolve automatically — log it in `OPEN_LOOPS.md` as an
unresolved conflict with both sources cited. This is a human decision point,
not an inference the skill should make.

# Reference: translating brand canon into deliverable-specific mandatories

Used in `SKILL.md` step 3 (Extract only relevant canon) and step 4 (Check
the request against canon for conflicts).

## The problem this solves
The failure mode is not "too little canon" — it's pasting the whole brand
book into the brief. A brief that repeats the brand's full voice guide,
color system and mission statement is not more on-brand than a short one; it
just makes the producer re-derive what actually applies to *this*
deliverable. A mandatory belongs in the brief only if violating it would be
a real production error for this specific asset.

## Which canon layer matters per deliverable type

| Deliverable type | Strategy | Verbal | Visual | Notes |
|---|---|---|---|---|
| Landing page / web | positioning, primary CTA logic | voice, headline conventions | full system: color roles, type scale, layout grid | Also pull any prior conversion data as a constraint, not a mandatory. |
| Social (Reel/post/campaign) | audience segment for this platform, offer | voice, caption conventions, hook patterns | motion/photography style, on-screen text rules | Platform-native format rules (see `deliverable-format-specs.md`) often override generic visual system defaults (e.g. vertical-only crops) — flag when they conflict. |
| Executive deck | positioning, proof points, the ask | voice (usually more formal register than consumer copy) | deck template, chart/data-viz style if defined | Audience is internal/investor, not the brand's end customer — do not import consumer-facing tone rules wholesale. |
| Packaging | claims policy, regulatory constraints | product-name conventions, ingredient/feature naming | full identity system + physical production specs (dieline, print process) | Legal/compliance canon is almost always mandatory here even if thin elsewhere. |
| Generated media (AI video/image) | — | voice for any on-screen/voiceover copy | visual system + explicit anti-patterns for generative artifacts (see below) | Add a mandatory anti-pattern section for generic-AI tells (stock-photo sameness, uncanny hands/text) even if canon doesn't mention generative media explicitly — extrapolate from the visual system's existing "avoid generic" rules rather than inventing new brand rules. |

## The genericization test
Before adding a mandatory to the brief, ask: *if you swapped this brand's
name for a direct competitor's, would this line still make sense?* If yes,
it's not a mandatory — it's generic creative advice and doesn't belong in
the brief. Cut it, or make it specific enough that it wouldn't survive the
swap (name the actual color, the actual banned phrase, the actual claim
threshold).

## Handling a request that conflicts with canon
When the deliverable request asks for something a locked canon rule
forbids (a banned claim, an off-voice tone, a visual treatment the identity
system rules out):
1. Do not quietly draft around it and also do not quietly comply — both
   hide the conflict from the person who asked.
2. Check whether canon is unambiguous about precedence (a hard legal/
   compliance rule always overrides a stylistic request; a stylistic
   canon rule does not automatically override a stated business need).
3. If canon resolves it, brief the canon-compliant version and record the
   override as a `decision` with the reason.
4. If canon does not resolve it (a judgment call, not a hard rule), leave it
   in `CREATIVE_BRIEF.md` § Open Flags and `RUN_RESULT.unresolved` — this is
   a decision for a human, not something to infer.

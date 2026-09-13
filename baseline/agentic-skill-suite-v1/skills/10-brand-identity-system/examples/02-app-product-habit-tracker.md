# Worked Example — App/Product Brand (habit-tracking mobile app)

`APPROVED_VISUAL_DIRECTION.md` (abbreviated): a consumer habit-tracking app
whose direction is "quiet momentum" — soft/approachable materiality
(rounded, low-contrast surfaces), color reserved for streak/progress
states only, imagery language is data-driven (progress rings/charts), no
photography. Motion: expressive on milestone completion, restrained
elsewhere.

## Step 1 — architecture (excerpt)
Wordmark-led lockup (no separate symbol mark at launch). X = cap-height of
the wordmark = 28px at the 200px-wide reference lockup. Clear space = 0.75X
(simple wordmark, less relief needed than a dense symbol) = 21px at
reference size. Minimum size: digital 88px lockup width (below this the
letterspacing collapses at typical device sizes); a monogram "first-letter"
variant is defined separately for the app-icon/favicon context.

## Step 2 — color roles (excerpt)
| Role | Token | Value | Usage rule | Approved pairing (computed) |
|---|---|---|---|---|
| Primary | `color.brand.primary` | `#0F766E` (teal) | Structural/interactive elements, primary CTA | on `#FFFFFF`: **5.47:1** — clears 4.5:1, approved for text/UI |
| Accent (streak signal) | `color.brand.accent` | `#FB7185` (coral) | Streak/celebration state fills only — never text or icon strokes | on `#FFFFFF`: **2.69:1**, on `#0F766E`: **2.03:1** — fails both thresholds against every approved surface; **decorative fill/illustration accent only, never text or UI** |
| Neutral-50…900 | `color.neutral.*` | `#F8FAF9`…`#08302C` | Backgrounds/structure | — |

Note the coral pairing: rather than dropping the accent color entirely (it
carries the "celebration" emotional signal the direction calls for), usage
is narrowed to non-text decorative fills (progress-ring celebration state,
illustration accents) and logged as an exception in step 7 — not silently
promoted to a text-approved color it cannot support.

## Step 3 — typography (excerpt)
Base 16px, ratio 1.2 (minor third — gentler step-up than the finance
example, matching the "quiet" mood). `type.scale.200` (body) = 16px/1.6
line-height/400. Rounded-terminal humanist sans (voice-forward, not purely
structural — direction calls the type "part of the personality").

## Step 4 — grid/spacing/shape (excerpt)
Radius: `radius.lg`=20px default card radius, `radius.full` for progress
rings/avatar — soft/approachable pole, opposite of the finance example,
each traced to its own direction's materiality axis rather than a shared
default. Iconography: 24px grid, 2px stroke, filled default (rounded/soft
pole, consistent with radius scale).

## Step 5 — motion
`motion.duration.fast`=150ms (routine interactions), `motion.duration.slow`
=480ms (milestone-completion celebration only) — trigger logic:
state-change-driven, with the celebration case as the direction's one
explicit "expressive" exception, restraint rule: no ambient/idle motion.

## Step 6 — application rules (5 surfaces)
Product/UI (iOS/Android), marketing site, social (Instagram/TikTok —
9:16 and 1:1, coral celebration accent used as illustration only, never as
on-image text color), App Store/Play Store listing assets, and email
(streak-reminder notifications, teal CTA only, per the pairing table).

## Step 9 — audit result
Coral's restricted (non-text) usage is stated identically in §2 and the
exceptions section; radius/iconography/type choices each cite the
materiality axis explicitly rather than reusing another brand's defaults;
5 surfaces covered; motion section states both the routine and the
milestone-exception cases rather than a single blanket duration.
`status: COMPLETE`.

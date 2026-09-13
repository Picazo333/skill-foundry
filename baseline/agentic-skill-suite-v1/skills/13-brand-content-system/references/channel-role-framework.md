# Reference: assigning channels a role instead of copy-pasting content

Used in `SKILL.md` step 5 (channel-role map) and `FORMAT_LIBRARY.md`'s
per-channel variants.

## The anti-pattern this exists to prevent
Posting the same asset, same length, same structure to every channel because
"we're already making it." This produces content that is native to no
channel and wastes the channel's own strengths (and its algorithm's
preferences).

## Assigning a role
For each channel in scope, answer three questions before any format is
written for it:

1. **Which pillar(s) does this channel actually serve well?** Not every
   pillar belongs on every channel. A channel with a short attention window
   and high scroll velocity (e.g. short-form vertical video feeds) tends to
   serve Attention/Trust pillars better than long-form Retention content;
   a channel with high dwell time and search intent (e.g. long-form video,
   blog/SEO) tends to serve Trust/Intent better than Attention.
2. **Which journey stage(s) does this channel's audience arrive at?** A
   channel that is mostly first-touch discovery should not be loaded with
   bottom-of-funnel conversion asks; a channel that is mostly existing-
   follower/owned-audience should not be treated as pure cold-attention
   inventory.
3. **What does the channel's native format force to change?** Length caps,
   vertical vs. horizontal, algorithm behavior (e.g. reward for completion
   rate vs. reward for comments/shares vs. reward for saves), caption vs.
   on-screen text conventions, whether links are clickable in-post.

## Applying it
`FORMAT_LIBRARY.md`'s channel-variant table exists because the answer to
question 3 changes the format archetype's hook/body/CTA even when the
underlying pillar and message stay identical. Document the change, not just
the fact that one exists — "shorter" is not a variant, "hook must land in
the first 1.5s with on-screen text because audio-off viewing is the norm on
this channel" is.

## Compliance interacts with channel role
Some channels carry additional platform-level restrictions on top of the
brand's own compliance boundaries (e.g. regulated-industry ad policies,
age-gating, platform content policies for gambling/health/finance verticals).
Check platform policy for the vertical in addition to `VERBAL_IDENTITY.md`'s
boundaries before assigning a pillar to a channel — a pillar may need a
different format variant, or may not be assignable to that channel at all.

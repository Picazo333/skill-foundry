# Design Token Naming Convention

Used in `SKILL.md` step 8 to build `DESIGN_TOKENS.json`. A consistent
naming scheme is what makes the token file directly consumable by a
design-token pipeline (Style Dictionary, Tokens Studio, a CSS variable
generator) instead of a bespoke one-off JSON shape.

## Pattern
```
<category>.<role>[.<variant>][.<scale-step>][.<property>]
```

## Categories and examples
| Category | Pattern | Examples |
|---|---|---|
| Color | `color.<group>.<role>[-<step>]` | `color.brand.primary`, `color.brand.accent`, `color.neutral.50`…`color.neutral.900`, `color.semantic.success`, `color.semantic.error` |
| Typography | `type.family.<role>`, `type.scale.<step>.<property>` | `type.family.primary`, `type.family.fallback`, `type.scale.100.fontSize`, `type.scale.100.lineHeight`, `type.scale.100.fontWeight` |
| Spacing | `space.<step>` | `space.1` … `space.10` (values increase monotonically with step number — never reorder) |
| Radius | `radius.<size>` | `radius.sm`, `radius.md`, `radius.lg`, `radius.full` |
| Border/stroke | `border.width.<size>` | `border.width.hairline`, `border.width.default`, `border.width.heavy` |
| Motion | `motion.duration.<speed>`, `motion.easing.<name>` | `motion.duration.fast`, `motion.duration.base`, `motion.duration.slow`, `motion.easing.standard` |
| Icon | `icon.<property>` | `icon.grid`, `icon.strokeWidth` |
| Logo | `logo.<property>` | `logo.clearSpace.unit`, `logo.minSize.digital`, `logo.minSize.print` |

## Rules
1. **Role, not appearance, names color tokens.** `color.brand.primary`, not
   `color.navy` — the hex can change under a rebrand without renaming every
   consumer. The literal value lives in the token's `value` field, not the
   name.
2. **Numeric scale steps are unitless and monotonic.** `space.4` is always
   larger than `space.3` regardless of the actual px value chosen for
   either — never renumber to "fix" a value later; add a new step instead.
3. **One token, one value.** `DESIGN_TOKENS.json`'s value for a given
   token name must be byte-identical to the value stated for it in
   `IDENTITY_SYSTEM.md`'s prose (`SKILL.md` step 8 requirement, checked in
   step 9's audit). If a value needs to change, change it in both places in
   the same edit.
4. **No orphan tokens, no orphan prose.** Every token that exists must be
   referenced by name somewhere in `IDENTITY_SYSTEM.md` or
   `APPLICATION_RULES.md`; every value with a name in the prose must have a
   matching token. This is checked mechanically in step 9.
5. **Sub-brand/multi-brand namespacing (`DEEP` mode).** Prefix the category
   with the sub-brand slug: `<subbrand>.color.brand.primary`. Shared/system
   tokens that apply across all sub-brands stay unprefixed.

## File shape
See `templates/DESIGN_TOKENS.json` for the exact structure: each token is
an object with `value`, `type`, and (where relevant) `description` fields,
grouped under its category as top-level keys.

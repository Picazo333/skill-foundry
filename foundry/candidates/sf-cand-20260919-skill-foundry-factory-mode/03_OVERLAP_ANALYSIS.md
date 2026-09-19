# G3 Overlap Analysis — Factory Mode

## REUSE
The existing `skill-foundry` front door already owns Foundry intent detection and recognizes FACTORY, but currently blocks it.

## EXTEND
**Recommended.** Extend the published front door so FACTORY routes to the canonical Factory workflow after G5.

## MODE
Factory is an operational mode within the same front-door responsibility, implemented by extending the existing package rather than creating a second Skill.

## NEW_SKILL
Rejected. A separate Factory Skill would duplicate the approved front-door boundary and encourage user-facing mode selection.

Decision: `EXTEND skill-foundry`.

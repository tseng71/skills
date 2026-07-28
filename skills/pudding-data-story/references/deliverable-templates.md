# Deliverable templates

Copy these structures into the project and fill them before implementation is considered complete.

## Contents

1. `story-brief.md`
2. `data-notes.md`
3. `storyboard.md`
4. `visual-system.md`
5. `qa-notes.md`
6. `implementation-traceability.md`
7. `design-contract.json`
8. `design-conformance.json`

## `story-brief.md`

```markdown
# Story brief

## Reader promise
In one sentence, what will the reader understand or experience?

## Driving question

## Evidence-backed thesis
Mark as provisional until the claim ledger is verified.

## Tension
What reasonable expectation does the evidence complicate?

## Audience
What can this reader already be expected to know?

## Human or concrete opening

## Visual reason
Why is this better seen or experienced than only written?

## Reader transformation
What should the reader notice, reconsider, or be able to do by the end?

## Scope and exclusions

## Ethical or representational risks
```

## `data-notes.md`

```markdown
# Data notes

## Sources
| Dataset | Owner | URL | Retrieved | License | Coverage |
|---|---|---|---|---|---|

## Claim ledger
| Claim/scene | Measure | Grain | Time range | Source | Transformation | Caveat |
|---|---|---|---|---|---|---|

## Transformations
Include formulas, denominators, units, filters, joins, and missing-value treatment.

## Quality checks
- duplicates:
- missingness:
- category drift:
- outliers:
- reconciliation:

## Limitations

## Reproduction
Commands or notebook order needed to rebuild the story data.
```

## `storyboard.md`

```markdown
# Storyboard

## Visual system
Persistent entities, encodings, scales, annotations, and mobile fallback.

| Beat | Reader-facing copy | Evidence | Visual state | State operation | Reader action | Transition meaning | Reduced-motion state |
|---|---|---|---|---|---|---|---|

## Exploratory state
Default, URL state, empty/error cases, and reset behavior.

## Ending
How the final state resolves the opening without overstating the evidence.
```

## `visual-system.md`

```markdown
# Visual system

## Visual noun
The persistent subject-specific entity the reader follows.

## Visual verb
How it changes: moves, splits, accumulates, ages, deviates, disappears, or another subject-native action.

## Subject material
Objects, imagery, symbols, sounds, paths, textures, or motion native to the topic.

## Comparison frame
Stable baseline, map, timeline, coordinate system, or other frame.

## State ladder
| State | Operation | Entities preserved | Encoding introduced | Claim | Key-frame sketch |
|---|---|---|---|---|---|

## Palette roles
| Color | Data/editorial role | Contrast check | Non-color cue |
|---|---|---|---|

## Typography and annotation
Tone, hierarchy, label behavior, and what must not be imitated.

## Desktop key frames
Opening, first encoding, central reveal, mechanism, exploration, and ending.

## Mobile redesign
Recomposition, control changes, sticky behavior, and content order. Do not write “same as desktop.”

## Reduced motion
Direct-state replacements for each meaningful transition.

## Ethical boundaries
What must not be gamified, aestheticized, exposed, or made anonymous.
```

## `qa-notes.md`

```markdown
# QA notes

## Build tested
Commit/version and date.

## Design conformance
- frozen design version:
- contract path:
- conformance report path:
- automatic repair iterations:
- local release-candidate result:
- public URL result:

## Data verification
| Displayed claim | Source row/calculation | Verified by | Result |
|---|---|---|---|

## Experience matrix
| Browser/device | Viewport | Scroll down/up | Controls | Keyboard | Reduced motion | Result |
|---|---:|---|---|---|---|---|

## Accessibility
- reading order:
- visible focus:
- graphic names/takeaways:
- color-independent cues:
- zoom:

## Performance
Device/profile, load size, layout shift, and interaction notes.

## Known limitations
```

## `implementation-traceability.md`

```markdown
# Implementation traceability

## Frozen design
- approved design version:
- design contract:
- manuscript version:
- implementation version:

## Scene mapping
| Scene id | Approved design source | Contract requirement ids | Data source | Code entry point | Desktop evidence | Mobile evidence | Reduced-motion evidence | Status | Approved deviation |
|---|---|---|---|---|---|---|---|---|---|

## Implementation decisions
Record choices that implement, but do not alter, the approved design.

## Approved deviations
Each entry must identify the exact user approval and corresponding contract/design update.
```

## `design-contract.json`

```json
{
  "schema_version": 1,
  "design_version": "02-storyboard-wireframes-v2",
  "design_sources": [
    "docs/02-storyboard-wireframes-v2.md",
    "docs/visual-system.md"
  ],
  "viewports": [
    { "id": "desktop", "width": 1440, "height": 900, "reduced_motion": false },
    { "id": "mobile", "width": 390, "height": 844, "reduced_motion": false },
    { "id": "mobile-reduced", "width": 390, "height": 844, "reduced_motion": true }
  ],
  "scenes": [
    {
      "id": "opening",
      "design_source": "docs/02-storyboard-wireframes-v2.md#opening",
      "route": "/story/",
      "trigger": { "kind": "load", "value": null },
      "required_viewports": ["desktop", "mobile", "mobile-reduced"],
      "requirements": {
        "copy": ["Approved reader-facing sentence"],
        "visual_entities": ["subject-specific visual noun"],
        "encodings": ["position encodes the approved measure"],
        "annotations": ["required caveat"],
        "controls": [],
        "motion": "approved transition meaning",
        "reduced_motion": "direct final state with the same explanation"
      },
      "assertions": [
        {
          "id": "opening-title",
          "kind": "text",
          "selector": "h1",
          "expected": "Approved title"
        }
      ]
    }
  ]
}
```

Use stable scene and assertion ids. Replace every example value; never leave placeholder copy in an approved contract.

## `design-conformance.json`

```json
{
  "schema_version": 1,
  "design_version": "02-storyboard-wireframes-v2",
  "implementation_version": "release-candidate-or-commit",
  "target_url": "http://localhost:4173/story/",
  "iterations": [
    {
      "number": 1,
      "failures": ["opening/opening-title"],
      "fixes": ["Corrected title binding"]
    }
  ],
  "results": [
    {
      "scene_id": "opening",
      "viewport_id": "desktop",
      "screenshot": "docs/conformance-screenshots/opening--desktop.png",
      "assertions": [
        {
          "id": "opening-title",
          "status": "pass",
          "evidence": "Exact text matched",
          "approval_ref": null
        }
      ],
      "visual_review": {
        "status": "pass",
        "evidence": "Composition, visual noun, encoding, annotation, and hierarchy match",
        "approval_ref": null
      }
    }
  ],
  "summary": {
    "status": "pass",
    "unresolved": 0,
    "blocked": 0
  }
}
```

Create one result for every contracted scene/viewport pair. `approved-deviation` requires a non-empty `approval_ref`; all other unapproved mismatches remain `fail`.

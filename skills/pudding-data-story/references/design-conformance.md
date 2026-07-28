# Design conformance

Use this reference to turn the approved Stage 3 design into enforceable Stage 5 and Stage 6 acceptance evidence.

## Contents

1. Contract principle
2. Required artifacts
3. Scene contract
4. Browser evidence
5. Automated repair loop
6. Visual comparison
7. Status rules
8. Publication gate

## Contract principle

Treat approved design documents as immutable inputs to implementation. Compile their testable decisions into `design-contract.json`; do not replace the documents with the contract.

Freeze:

- approved design document paths and versions;
- stable scene ids;
- route and deterministic trigger for each scene;
- reader-facing copy that must appear;
- visual entities and encodings;
- annotations and caveats;
- controls and expected outcomes;
- transition meaning and final state;
- desktop, mobile, and reduced-motion requirements;
- structural or data assertions that browser automation can evaluate.

The contract describes the approved outcome. It must not contain implementation results, pass/fail statuses, or retroactive descriptions of what the code happens to do.

## Required artifacts

Keep these in the story repository:

```text
docs/
  01-concept-design-v1.md
  02-storyboard-wireframes-v2.md
  visual-system.md
  design-contract.json
  design-conformance.json
  implementation-traceability.md
  qa-notes.md
  conformance-screenshots/
    opening--desktop.png
    opening--mobile.png
    opening--mobile-reduced.png
```

Use the copy-ready JSON shapes in `deliverable-templates.md`. Store screenshot paths relative to the project root.

## Scene contract

Give every authored and exploratory key state a stable id. At minimum contract:

- opening;
- first taught encoding;
- central reveal;
- mechanism;
- each materially different interaction result;
- exploration default;
- ending;
- empty, loading, error, and fallback states when they can occur.

Every scene must declare:

- its approved design source;
- the route;
- a deterministic trigger such as load, step id, query state, or control sequence;
- required viewport ids;
- required copy, visual entities, encodings, annotations, controls, and reduced-motion outcome;
- assertions with stable ids.

Prefer semantic assertions:

- exact or normalized reader-facing text;
- existence and count of meaningful marks;
- `data-scene-id` and `data-state-*` values;
- scale domains, thresholds, selected ids, and displayed data values;
- control name, role, value, enabled state, and outcome;
- accessible graphic name and text takeaway.

Do not use brittle selectors or arbitrary pixel positions as the only proof. Add stable test hooks that describe meaning, not internal component names.

## Browser evidence

Use Playwright or the available browser-testing tool to:

1. build and serve the release candidate;
2. enter every scene through its contracted trigger;
3. wait for fonts, data, layout, and meaningful transitions to settle;
4. assert the contracted DOM, state, text, data, control, and accessibility outcomes;
5. capture a full final-state screenshot for every required viewport;
6. repeat required scenes with reduced motion;
7. test backscroll, direct reload, and interaction reset where contracted;
8. write results to `design-conformance.json`.

Capture at deterministic viewport sizes. Disable unrelated time-, cursor-, random-, or network-dependent variation. Seed simulations. Do not hide a failing element before taking the screenshot.

Expose `data-scene-id` on the primary graphic and stable state attributes when they improve verification. These attributes are diagnostic semantics, not reader-facing copy.

## Automated repair loop

After the first implementation:

1. run the static build and technical audit;
2. run all contracted browser checks;
3. inspect every screenshot against the approved key frame and scene criteria;
4. classify each failure;
5. fix implementation-level failures;
6. rerun the build and every affected check;
7. rerun the complete suite before preview or publication;
8. continue without asking for routine confirmation.

Automatically fix:

- missing or incorrect copy already settled in the manuscript;
- wrong data bindings, calculations, labels, annotations, or caveats;
- missing visual entities or encodings;
- incorrect scene ordering or state transitions;
- layout, overlap, clipping, contrast, responsive, and sticky defects;
- broken controls, keyboard behavior, backscroll, reload, or reduced motion;
- implementation drift from approved palette, typography roles, spacing, and composition;
- build, base-path, prerender, asset, or public-route defects.

Do not automatically:

- change the thesis or evidence;
- remove an approved scene because it is difficult to implement;
- simplify the visual grammar into a different design;
- replace real data with synthetic values;
- edit the frozen contract to match the code;
- approve a deviation on the user's behalf.

Stop only when the required fix needs a design/evidence decision, external access is blocked, or five repair iterations fail to resolve the same issue. Report the scene, failed requirement, evidence, attempted fixes, and smallest proposed design change.

## Visual comparison

Visual conformance is semantic first and pixel-aware second.

For every screenshot, compare:

- composition and information hierarchy;
- presence, identity, and continuity of the visual noun;
- visual verb and final state of the transition;
- mark type, scale, axis, encoding, grouping, and annotation;
- required copy and caveats;
- palette roles, contrast, typography hierarchy, and density;
- desktop/mobile recomposition;
- reduced-motion explanatory equivalence;
- absence of clipping, overlap, unintended empty space, loading residue, or debug UI.

Use image or browser inspection for this comparison. Use pixel or snapshot differences only when the approved reference is sufficiently deterministic. A low pixel difference cannot override a semantic failure, and a responsive but semantically faithful layout must not fail only because line wrapping differs.

Record concise evidence and the screenshot path. Never record `pass` without opening the screenshot.

## Status rules

Use only:

- `pass` — implementation matches the contracted requirement;
- `approved-deviation` — it differs, but the user explicitly approved the exact deviation;
- `fail` — it does not match;
- `blocked` — verification cannot run because a required dependency or access path is unavailable.

`approved-deviation` requires a non-empty approval reference pointing to the conversation decision or versioned design update. “Equivalent,” “close enough,” or “intentional” is not a passing status by itself.

The conformance report passes only when:

- its design version equals the frozen contract;
- every scene/viewport pair has a result;
- every required screenshot exists and is non-empty;
- every assertion passes;
- every visual review is `pass` or an explicitly `approved-deviation`;
- unresolved failures and blockers equal zero.

Run `scripts/audit_design_conformance.py` to enforce this completeness gate.

## Publication gate

Stage 5 preview begins only after the local release candidate passes. Stage 6 publication completes only after the deployed public URL passes the same frozen contract.

If public verification fails:

1. fix the implementation or deployment configuration;
2. rebuild and redeploy;
3. rerun the failed checks;
4. rerun the complete contract;
5. update evidence to the final deployed version.

Do not publish first and defer conformance work. Do not report a local pass as a public-URL pass.

---
name: pudding-data-story
description: Build or revise reader-first interactive data stories and visual essays in the spirit of The Pudding. Use for Pudding-style websites, scrollytelling, scroll-driven graphics, interactive data journalism, data-backed longform features, animated visual explanations, storyboards, or audits of work that feels like a dashboard or ordinary chart. Also trigger for 中文 requests mentioning 数据叙事、滚动叙事、交互可视化、动态数据故事、Pudding 水准, or “不要像普通图表”. Covers editorial framing, evidence, substantive longform content, subject-specific visual grammar, staged design approval, versioned documents, Svelte 5 implementation, automatic design-conformance repair, GitHub-first publication, accessibility, mobile behavior, deployment, and QA.
---

# Pudding Data Story

Create visual journalism in which the reader experiences an argument through evidence. Treat motion and interaction as explanatory grammar, not decoration.

A finished story must be **substantive, documented, traceable, and publicly deployable**. Do not produce a thin showcase, a decorative demo, a dashboard with scrolling, or a page whose visuals are richer than its reporting.

Build every new standalone story on the current Svelte 5 Pudding-starter architecture: SvelteKit static prerendering, a runes-based story-state layer, and sticky scrollytelling. Deviate only for an existing application or a documented deployment constraint, and record the reason in the approved overall design. Never silently substitute a simpler HTML/CSS/JavaScript implementation.

Read [references/narrative-visual-grammar.md](references/narrative-visual-grammar.md) before proposing the visual concept or storyboard. It distills recurring patterns from close reading of 11 live Pudding stories. Use [references/pudding-examples.md](references/pudding-examples.md) to select the closest structural precedents.

## Start with the editorial gate

Do not begin with a chart type or animation. Establish:

- the driving question;
- a one-sentence thesis that the available data can support;
- what the reader should notice, understand, or reconsider;
- one concrete person, place, object, or event that can open the story;
- the data needed for every factual claim;
- why this story is better seen or experienced than merely written.

Reject or reframe a concept if it is only “a dashboard about X,” a tour of available metrics, or a generic trend recap. A strong story has an argument, human stakes, and a visual reason to exist.

Write to the reader. Never expose the design brief in published copy. Remove phrases such as “this visualization demonstrates,” “push the data,” “choose a lens,” “same group of particles,” “这里展示,” “推动数据,” or “观察镜头” unless the interface literally requires that instruction.

Read [references/editorial-workflow.md](references/editorial-workflow.md) before drafting the story structure.
For AI model, training-cost, benchmark, or capability stories, also read [references/ai-data-evidence.md](references/ai-data-evidence.md).

## Build substance before spectacle

Do not reduce a full story to a striking introduction, one reveal, and a generic explorer. Give the thesis enough authored evidence to feel earned:

- identify 3–6 substantive findings or explanatory beats, fewer only when the concept is intentionally narrow;
- pair every major pattern with a concrete example, mechanism, consequence, or counterexample;
- include historical, institutional, scientific, or cultural context when it changes interpretation;
- preserve contradictory evidence and exceptions that materially bound the thesis;
- keep methods concise in the narrative but complete in the documentation;
- cut repetition, not necessary depth.

Judge richness by the number of meaningful reader discoveries and how well they connect—not by scroll length, chart count, or word count.

## Verify the evidence

Build a claim-to-source ledger before implementation:

| Claim or scene | Measure | Grain | Time range | Source | Transformation | Caveat |
|---|---|---|---|---|---|---|

For every derived value, preserve units, denominator, missing-value treatment, filters, and calculation. Label estimates and incomplete coverage in the same visual state where they appear. Keep methodology and data downloads accessible without interrupting the main narrative.

If data is missing, stale, contradictory, or too coarse for the proposed claim, stop and narrow the claim. Do not animate uncertainty away.

## Non-negotiable workflow: six approval gates

For a new full story, follow these stages in order. Do not begin the next stage until the user explicitly confirms the current stage. A brief “confirm/确认” approves only the stage currently presented. Honor an explicit request to skip or combine stages.

Within an approved stage, work autonomously through implementation, validation, and correction. Do not pause for routine fixes or ask the user to repeat the same instruction. Pause only when a fix would change the approved thesis, evidence, narrative architecture, visual language, or another decision that requires a new approval.

### Stage 1 — Topic and editorial direction

Produce 3–6 viable angles when the topic is not fixed, then specify the driving question, provisional thesis, concrete opening, visual reason, likely data/reporting sources, reader value, evidence risks, scope, and estimated active reading time.

Save `docs/story-brief.md` or an equivalent project document. Stop for **topic/editorial direction confirmation**. Do not deeply research, design screens, or write production code first.

### Stage 2 — Overall story and visual design

After Stage 1 approval, specify:

- audience, editorial promise, narrative arc, chapters, central reveal, stakes, and ending;
- central visual noun and verb;
- subject-specific visual material and art direction;
- visual state ladder and how the first encoding is taught;
- interaction strategy and the authored-to-exploratory handoff;
- evidence, methodology, uncertainty, mobile, accessibility, and production plans;
- the Svelte 5 technical profile, or a documented exception for an existing application;
- content-depth and active-reading-time targets;
- repository structure and publishing plan.

Save `docs/overall-design.md` and `docs/visual-system.md`. Stop for **overall design confirmation**. Do not create detailed wireframes or production code first.

### Stage 3 — Detailed storyboard and key-frame design

After Stage 2 approval, create:

- a complete beat-by-beat storyboard with reader-facing draft copy;
- evidence attached to every factual scene;
- desktop and mobile layouts for every major scene;
- opening, first encoding, central reveal, mechanism, exploration, and ending key frames;
- visual-state and semantic-operation tables;
- scroll, interaction, transition, chart/map encoding, caveat, fallback, error, and reduced-motion states;
- an acceptance checklist;
- a machine-readable `design-contract.json` with stable scene ids, required viewports, approved copy, visual entities, encodings, annotations, interactions, motion behavior, reduced-motion behavior, and testable assertions.

Save versioned documents such as:

```text
docs/
  01-concept-design-v1.md
  02-storyboard-wireframes-v2.md
  visual-system.md
  design-contract.json
  implementation-traceability.md
```

Present the actual key frames or wireframes in the conversation, not only a verbal description. Stop for **detailed design confirmation**. Do not write the production webpage first.

### Stage 4 — Content, evidence, and data package

After Stage 3 approval, complete and version:

- `manuscript.md` — continuous publication-quality copy;
- `data-notes.md` or `methodology.md`;
- `sources.md`;
- processed local data and a data dictionary;
- the claim-to-source ledger;
- `implementation-traceability.md`, mapping scenes to approved design, code, and data;
- a frozen design-contract version that identifies the approved design documents it represents.

Meet the approved reading-time target with genuine reporting and explanation. For a flagship story, default to roughly 8–12 minutes of active reading unless the approved design specifies otherwise.

Stop for **content and evidence confirmation**. Do not begin production coding until the documents exist in the project repository and this stage is approved.

### Stage 5 — Implementation preview

After Stage 4 approval, implement strictly from the approved documents. Keep content, data, visual state, and rendering logic separated; never silently replace missing data with synthetic values; build desktop and mobile together.

Before presenting the preview, run the automatic design-conformance loop:

1. build the story and expose deterministic scene ids;
2. use browser automation to visit every contracted scene in every required viewport and reduced-motion mode;
3. capture final-state screenshots and run structural, copy, interaction, data, accessibility, stack, and visual comparisons against the frozen contract;
4. write `design-conformance.json` and update `implementation-traceability.md`;
5. fix every implementation-level failure without pausing;
6. rebuild, recapture, and rerun all affected checks;
7. repeat until all contracted results pass or are covered by a specifically approved deviation.

Do not weaken a test, edit the frozen contract, change the approved design, or label a mismatch “equivalent” merely to make the audit pass. If a faithful fix is impossible after five repair iterations, or requires changing an approved decision, stop with the exact blocker and proposed design change.

Only after the loop passes, provide the working preview plus a compact conformance summary and representative desktop/mobile screenshots. Stop for **implementation preview confirmation**.

### Stage 6 — QA, publication, and handoff

After Stage 5 approval:

1. complete all quality gates and rerun the automatic conformance loop against the release build;
2. commit source, data, approved design/research documents, the frozen contract, and conformance evidence;
3. publish to GitHub and deploy with GitHub Pages unless the user chose another target;
4. run the same contracted browser checks against the public URL;
5. automatically fix, rebuild, redeploy, and retest any implementation or deployment mismatch;
6. update README status, version/release notes, QA notes, conformance report, and traceability;
7. return repository, public story, design-document, methodology, source, and conformance-report links.

Do not claim publication or completion until the public URL has passed the frozen design contract. An unresolved, unapproved deviation is a release blocker.

When revising an already published story, diagnose and document structural changes first. Ask for approval when the revision changes thesis, narrative architecture, visual language, or publication state; do not manufacture gates for small fixes.

## GitHub-first source of truth

GitHub is the default source of truth for projects created with this skill. Keep the implementation and the documents that justify it together. A multi-story site should normally use one folder per story unless the repository already has another clear convention.

At minimum preserve:

```text
README.md
PUBLISHING.md
.github/workflows/pages.yml
docs/
  story-brief.md
  overall-design.md
  visual-system.md
stories/<story-slug>/
  application source
  data/
  assets/
  docs/
    01-concept-design-v1.md
    02-storyboard-wireframes-v2.md
    manuscript.md
    methodology.md
    sources.md
    design-contract.json
    design-conformance.json
    implementation-traceability.md
    qa-notes.md
    conformance-screenshots/
```

Commit approved design documents before production code. Preserve version history. README must state the real status—concept, prototype, release candidate, or published. Never describe a prototype as complete.

## Storyboard as a visual argument

Use the sequence:

1. **Concrete opening** — begin with a specific example the reader can grasp.
2. **Reveal** — show the first surprising relationship with minimal annotation.
3. **Zoom out** — place the example inside the full dataset.
4. **Mechanism** — explain why the pattern happens.
5. **Agency** — let the reader search, compare, simulate, or contribute when that action answers a real question.
6. **Stakes** — connect the pattern to people or consequences.
7. **Resolution** — return to the thesis with limits and a useful next thought.

For every beat, specify:

| Beat | Reader-facing copy | Evidence | Visual state | State operation | Reader action | Transition meaning |
|---|---|---|---|---|---|---|

One scroll step should make one claim. Scrollytelling is not a slideshow of chart types.

Define a persistent **visual noun** (the thing the reader follows) and **visual verb** (what it does: moves, accumulates, splits, ages, deviates, disappears). Build the central visual through meaningful operations such as instantiate, demonstrate, duplicate, align, encode, reorder, annotate, aggregate, mechanize, explore, and return.

Teach the visual grammar before revealing a dense chart. Introduce one mark, property, axis, threshold, or comparison at a time. Let the reader see the chart being assembled from recognizable examples, then hand over exploratory controls.

## Match visual form to the argument

Choose encodings from the comparison the reader must make:

- change over time → line, connected position, or animated trajectory;
- distribution or uncertainty → dots, density, interval, or simulation;
- part-to-whole → aligned bars or area only when precise comparison is not central;
- flow or transformation → sankey, alluvial, or stable marks that move between states;
- geography → map only when location explains the pattern;
- sequence or conversation → synchronized timeline;
- friction or constraints → simulation or playable model when the interaction embodies the thesis;
- individual examples within a population → concrete-first small multiple, beeswarm, or searchable field.

Preserve object constancy only for the same semantic entities. Do not morph unrelated metrics into “the same particles.” Avoid chart carousels, gratuitous 3D, decorative network graphs, and motion that adds no meaning.

Read [references/interaction-patterns.md](references/interaction-patterns.md) when selecting a visual or interaction.

## Create a subject-specific visual world

Do not imitate The Pudding's surface styling or use a generic “data journalism” skin. Derive a visual system from the subject:

- turn meaningful objects, people, sounds, paths, or shapes into the marks;
- keep illustration and statistical graphics in one visual language;
- use a restrained palette where analytical colors have explicit roles;
- vary density and scale across the story so every section is not equally loud;
- redesign the composition for mobile instead of shrinking desktop;
- preserve the subject-specific material when the story reaches abstract data.

Reject an art direction that could fit an unrelated topic after changing only the labels.

## Use motion as a sentence

Every transition must answer one of:

- What changed?
- Where did this item go?
- How does this subset differ?
- What happens under this assumption?
- How does a specific example relate to the whole?

Prefer stable marks that move, sort, aggregate, split, or annotate. Use fades only as support. Avoid ambient loops after the reader has understood the state.

Scrolling backward must restore the prior state. Keep transitions interruptible. Respect `prefers-reduced-motion`; reduced motion must preserve the explanation through direct state changes, not remove content.

## Make interaction earn its place

An interaction belongs only if it lets the reader:

- find themselves or a meaningful example;
- compare alternatives;
- test a causal or policy mechanism;
- inspect evidence that would clutter the default view;
- contribute data to a clearly explained experiment.

Provide a meaningful default state. Label controls in audience language. Do not make readers click merely to continue reading, and do not hijack wheel, trackpad, touch, or keyboard behavior.

Search, filter, scrub, sort, and simulation controls must change real data dimensions. A control that only swaps decorative scenes should be removed or turned into authored scroll progression.

Prefer the sequence **author a strong default → teach the encoding → reveal the full field → let the reader explore**. Do not open with a blank tool unless search itself is the natural reader question. If opening with a choice, allow the reader to skip and preserve the choice for a later payoff.

## Use the Svelte 5 production baseline

For every new standalone story, inspect the current [Pudding website starter](https://github.com/the-pudding/website), record the versions used, and implement this baseline:

- Svelte 5 in runes mode;
- SvelteKit with `@sveltejs/adapter-static`, route-level prerendering, and a verified static build;
- a `.svelte.js` or `.svelte.ts` state layer using `$state` for authored and exploratory inputs, `$derived` for the complete visual state, and `$effect` only for external synchronization;
- a reusable `Scrolly.svelte` component, CSS `position: sticky`, and IntersectionObserver for discrete steps;
- deterministic rendering from the complete state so backscroll and refresh restore the correct scene;
- preprocessed CSV/JSON/SVG data, with D3 or LayerCake for scales, layout, and custom marks when useful;
- GitHub Pages base-path and trailing-slash handling when Pages is the target.

Keep authored scroll state separate from reader-controlled exploration. Do not drive dozens of SVG mutations directly from the observer, use legacy stores as the primary story-state layer, update component state on every raw scroll event, or make `$effect` the source of derived visual truth.

For an existing React, Next.js, Vue, Sites, CMS, or legacy story, preserve its stack only when replacement would be disproportionate or the user approves the exception. Record the reason and reproduce the same boundaries:

1. normalized data;
2. authored and exploratory inputs;
3. derived complete visual state;
4. deterministic renderer;
5. scroll and control adapters;
6. reader-facing copy, methods, and sources.

Technical fidelity does not replace editorial or visual quality. Do not reproduce The Pudding's logo, house fonts, or visual identity. Its code starter is a technical reference, not a brand template.

Read [references/technical-template.md](references/technical-template.md) before Stage 5 implementation.

## Build mobile and accessibility in from the first state

- Use semantic headings and a linear reading order that works without animation.
- Provide keyboard access and visible focus for every control.
- Give SVG graphics an accessible name and a concise text takeaway.
- Use color plus another cue; never color alone.
- Make touch targets at least 44 CSS pixels.
- Avoid fixed `100vh` scrolly geometry on mobile browser chrome; prefer content-driven sizing and `svh`/`dvh` with fallbacks.
- Ensure sticky graphics do not cover text or trap interactive controls.
- Provide a static or step-based fallback when sticky positioning or observers fail.
- Test 320 px, 768 px, and wide desktop layouts, plus portrait and landscape.

## Quality gates

Before declaring the story complete:

1. Run `python scripts/audit_story.py <project-or-story-file> --strict-stack` for a new standalone story; omit `--strict-stack` only for an approved existing-stack exception.
2. Run `python scripts/audit_design_conformance.py <design-contract.json> <design-conformance.json> --root <project-directory>`.
3. Read every visible sentence as a reader; remove production language and design rationale.
4. Verify every displayed number against the source or transformation.
5. Scroll down and back up slowly and quickly; test refresh at every contracted deep state.
6. Use every control with mouse, keyboard, and touch-size viewport.
7. Test reduced motion and a no-JavaScript or failed-observer fallback.
8. Compare every contracted desktop and mobile screenshot with its approved key frame and acceptance criteria.
9. Verify performance on a mid-range mobile profile; avoid per-frame DOM churn.
10. Verify all internal and source links.
11. Confirm README status, frozen design version, conformance report, and implementation traceability match reality.
12. Confirm the GitHub Pages workflow completes and rerun the contract against the public URL.

Use [references/pudding-examples.md](references/pudding-examples.md) as a pattern library, not a style catalog. Copy the editorial logic, not the surface.
Read [references/design-conformance.md](references/design-conformance.md) before building Stage 3 acceptance criteria or running Stage 5 and Stage 6.

## Required handoff

Deliver:

- `story-brief.md` and `overall-design.md`;
- versioned concept, storyboard, and wireframe documents;
- `visual-system.md` — visual noun/verb, subject material, palette roles, typography, state ladder, key frames, mobile and reduced-motion designs;
- `manuscript.md`;
- `data-notes.md` or `methodology.md`, plus `sources.md`;
- local processed data, data dictionary, and claim ledger;
- frozen `design-contract.json`;
- `design-conformance.json` and all contracted screenshots;
- `implementation-traceability.md`;
- the implemented story;
- `qa-notes.md` — device, accessibility, interaction, data, and deployment checks;
- GitHub repository URL and verified public story URL.

Use the copy-ready structures in [references/deliverable-templates.md](references/deliverable-templates.md). Do not leave a template field blank without explaining why it does not apply.

When revising an existing story, diagnose it against these gates first. Produce revised design documents at the appropriate stage, obtain confirmation, then implement. Do not retrofit a page first and reconstruct its rationale afterward.

---
name: pudding-data-story
description: Build or revise reader-first interactive data stories and visual essays in the spirit of The Pudding. Use for Pudding-style websites, scrollytelling, scroll-driven graphics, interactive data journalism, data-backed longform features, animated visual explanations, storyboards, or audits of work that feels like a dashboard or ordinary chart. Also trigger for 中文 requests mentioning 数据叙事、滚动叙事、交互可视化、动态数据故事、Pudding 水准, or “不要像普通图表”. Covers editorial framing, evidence, substantive longform content, subject-specific visual grammar, staged design approval, versioned documents, GitHub-first implementation, accessibility, mobile behavior, deployment, and QA.
---

# Pudding Data Story

Create visual journalism in which the reader experiences an argument through evidence. Treat motion and interaction as explanatory grammar, not decoration.

A finished story must be **substantive, documented, traceable, and publicly deployable**. Do not produce a thin showcase, a decorative demo, a dashboard with scrolling, or a page whose visuals are richer than its reporting.

Base new standalone work on The Pudding's official website starter when its stack fits. In an existing codebase, preserve the stack and port the starter's patterns instead of replacing the application.

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
- an acceptance checklist.

Save versioned documents such as:

```text
docs/
  01-concept-design-v1.md
  02-storyboard-wireframes-v2.md
  visual-system.md
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
- `implementation-traceability.md`, mapping scenes to approved design, code, and data.

Meet the approved reading-time target with genuine reporting and explanation. For a flagship story, default to roughly 8–12 minutes of active reading unless the approved design specifies otherwise.

Stop for **content and evidence confirmation**. Do not begin production coding until the documents exist in the project repository and this stage is approved.

### Stage 5 — Implementation preview

After Stage 4 approval, implement strictly from the approved documents. Keep content, data, visual state, and rendering logic separated; update traceability when implementation differs; never silently replace missing data with synthetic values; build desktop and mobile together.

Provide a working preview or representative screenshots covering the opening, central reveal, and exploratory state. Stop for **implementation preview confirmation**.

### Stage 6 — QA, publication, and handoff

After Stage 5 approval:

1. complete all quality gates and fix blocking defects;
2. commit source, data, and approved design/research documents;
3. publish to GitHub and deploy with GitHub Pages unless the user chose another target;
4. verify the public URL, central interactions, desktop, and mobile;
5. update README status, version/release notes, and traceability;
6. return repository, public story, design-document, methodology, and source links.

Do not claim publication or completion until the public URL has been checked.

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
    implementation-traceability.md
    qa-notes.md
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

## Implement with the official-template model

For a new Svelte story, inspect the current state of [The Pudding website starter](https://github.com/the-pudding/website) before copying patterns; it is an active Svelte migration. Use its architecture as the default:

- preprocessed CSV/JSON/SVG imports;
- Svelte components and stores for viewport/scroll state;
- a reusable `Scrolly` component;
- CSS `position: sticky` for the graphic;
- IntersectionObserver or Scrollama for discrete steps;
- D3/LayerCake for custom marks, scales, and layout;
- static/SSR output where practical;
- ArchieML or an equivalent content workflow when editors need structured copy.

For React, Next.js, Sites, or another existing stack, reproduce the same separation of concerns:

1. normalized data;
2. derived story states;
3. a pure visual renderer;
4. scroll/interaction state;
5. reader-facing copy;
6. methods and sources.

Do not reproduce The Pudding's logo, house fonts, or visual identity. The official starter is MIT-licensed, but its README explicitly excludes brand assets.

Read [references/technical-template.md](references/technical-template.md) before implementation.

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

1. Run `python scripts/audit_story.py <project-or-story-file>`.
2. Read every visible sentence as a reader; remove production language and design rationale.
3. Verify every displayed number against the source or transformation.
4. Scroll down and back up slowly and quickly; test refresh at a mid-story URL position.
5. Use every control with mouse, keyboard, and touch-size viewport.
6. Test reduced motion and a no-JavaScript or failed-observer fallback.
7. Check that the opening, central reveal, and ending remain understandable in screenshots.
8. Verify performance on a mid-range mobile profile; avoid per-frame DOM churn.
9. Verify all internal and source links.
10. Confirm README status and implementation traceability match reality.
11. Confirm the GitHub Pages workflow completes.
12. Open the public homepage and story URL.

Use [references/pudding-examples.md](references/pudding-examples.md) as a pattern library, not a style catalog. Copy the editorial logic, not the surface.

## Required handoff

Deliver:

- `story-brief.md` and `overall-design.md`;
- versioned concept, storyboard, and wireframe documents;
- `visual-system.md` — visual noun/verb, subject material, palette roles, typography, state ladder, key frames, mobile and reduced-motion designs;
- `manuscript.md`;
- `data-notes.md` or `methodology.md`, plus `sources.md`;
- local processed data, data dictionary, and claim ledger;
- `implementation-traceability.md`;
- the implemented story;
- `qa-notes.md` — device, accessibility, interaction, data, and deployment checks;
- GitHub repository URL and verified public story URL.

Use the copy-ready structures in [references/deliverable-templates.md](references/deliverable-templates.md). Do not leave a template field blank without explaining why it does not apply.

When revising an existing story, diagnose it against these gates first. Produce revised design documents at the appropriate stage, obtain confirmation, then implement. Do not retrofit a page first and reconstruct its rationale afterward.

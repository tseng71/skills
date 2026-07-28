---
name: pudding-data-story
description: Build or revise reader-first interactive data stories and visual essays in the spirit of The Pudding. Use for Pudding-style websites, scrollytelling, scroll-driven graphics, interactive data journalism, data-backed longform features, animated visual explanations, storyboards, or audits of work that feels like a dashboard or ordinary chart. Also trigger for 中文 requests mentioning 数据叙事、滚动叙事、交互可视化、动态数据故事、Pudding 水准, or “不要像普通图表”. Covers editorial framing, evidence, detailed longform content, staged design approval, versioned design documents, GitHub-first implementation, accessibility, mobile behavior, deployment, and QA.
---

# Pudding Data Story

Create visual journalism in which the reader experiences an argument through evidence. Treat motion and interaction as explanatory grammar, not decoration.

A finished story must be **substantive, documented, traceable, and publicly deployable**. Do not produce a thin showcase, a decorative demo, a dashboard with scrolling, or a page whose visuals are richer than its reporting.

Base new standalone work on The Pudding's official website starter when its stack fits. In an existing codebase, preserve the stack and port the starter's patterns instead of replacing the application.

## Non-negotiable workflow: staged approval gates

For a new story, follow the stages below in order. **Do not begin the next stage until the user explicitly confirms the current stage.** A confirmation applies only to the named stage; do not treat one confirmation as approval for later stages.

### Stage 1 — Topic and editorial direction

Produce a topic proposal containing:

- 3–6 viable story angles when the topic is not yet fixed;
- the driving question;
- a one-sentence thesis supported by obtainable evidence;
- the human opening;
- why the story must be visual or interactive;
- likely datasets and reporting sources;
- expected reader value;
- major evidence risks;
- recommended scope and estimated reading time.

Stop and ask for **topic/editorial direction confirmation**.

Do not research deeply, design screens, write production code, or create a repository structure before this confirmation.

### Stage 2 — Overall story design

After Stage 1 approval, produce a detailed overall design that includes:

- audience and editorial promise;
- narrative arc;
- chapter list and purpose of every chapter;
- central reveal;
- proposed visual grammar;
- interaction strategy;
- evidence plan;
- mobile strategy;
- accessibility strategy;
- content depth target;
- expected active reading time;
- data, methodology, and uncertainty plan;
- production architecture;
- GitHub repository and publishing plan.

Save this as `docs/overall-design.md` or an equivalent project-level document.

Stop and ask for **overall design confirmation**.

Do not create detailed wireframes or begin implementation before this confirmation.

### Stage 3 — Detailed storyboard and visual design

After Stage 2 approval, create a complete, development-ready design package. It must contain:

- beat-by-beat storyboard;
- reader-facing draft copy for every scene;
- evidence attached to every factual scene;
- desktop layout or wireframe for every major scene;
- mobile layout for every major scene;
- visual state table;
- scroll and interaction states;
- transition meaning;
- chart or map encoding rules;
- data properties and caveats;
- empty, loading, fallback, and error states where relevant;
- reduced-motion behavior;
- acceptance checklist.

Save the package as versioned documents, for example:

```text
docs/
  01-concept-design-v1.md
  02-storyboard-wireframes-v2.md
  implementation-traceability.md
```

Present the detailed design to the user and stop for **detailed design confirmation**.

Do not write the production webpage before this confirmation.

### Stage 4 — Content, evidence, and data package

After Stage 3 approval, complete and version:

- `manuscript.md` — continuous, publication-quality copy;
- `data-notes.md` or `methodology.md` — sources, transformations, units, caveats, uncertainty;
- `sources.md` — source list and citation notes;
- processed local data files;
- data dictionary;
- claim-to-source ledger;
- implementation traceability table mapping scenes to code and data.

The content must be sufficiently rich for the approved reading-time target. Do not pad with repetition, but do not compress a longform story into captions and slogans. For a typical flagship story, target roughly **8–12 minutes of active reading**, unless the approved design specifies otherwise.

Stop and ask for **content and evidence confirmation**.

Do not begin production coding until the documents above exist in the project repository and the user has approved this stage.

### Stage 5 — Implementation preview

After Stage 4 approval:

- implement strictly from the approved documents;
- keep content, data, visual state, and rendering logic separated;
- update `implementation-traceability.md` whenever implementation differs from design;
- never silently replace missing formal data with synthetic values;
- clearly label any scenario, estimate, model, or demonstration;
- build desktop and mobile together;
- provide a working preview or screenshots of representative scenes.

Stop and ask for **implementation preview confirmation** before declaring the story final or publishing the production release.

### Stage 6 — QA, GitHub publication, and handoff

After Stage 5 approval:

1. complete the quality gates in this skill;
2. fix all blocking defects;
3. ensure all design and research documents are committed;
4. publish source code and documents to GitHub;
5. deploy the public webpage through GitHub Pages unless the user explicitly chooses another GitHub-compatible target;
6. verify the public URL, main interactions, desktop layout, and mobile layout;
7. update README, version, release notes, and traceability status;
8. return the GitHub repository URL, public webpage URL, design-document links, and known limitations.

Do not claim publication or completion until the public URL has been checked. If deployment cannot be verified, state that clearly.

## GitHub-first source of truth

GitHub is the default source of truth for every project created with this skill.

The repository must contain both the website and the documents that justify it. At minimum:

```text
README.md
PUBLISHING.md
.github/workflows/pages.yml
index.html or application source

docs/
  overall-design.md
  editorial-principles.md or story brief

stories/<story-slug>/
  index.html or application source
  styles / components / scripts
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

Rules:

- commit approved design documents before production code;
- preserve version history instead of overwriting all design rationale into one summary;
- every major visual module must map to a design section, code location, data source, and completion status;
- README must state the true project status: concept, prototype, release candidate, or published version;
- never describe a prototype as complete;
- GitHub Pages deployment configuration must live in the repository;
- the final handoff must include direct links to the repository, story, design documents, methodology, and sources.

## Content must be substantive

A Pudding-style story is not merely an animated page. It must contain enough reporting and explanation to support the reader's understanding.

Required content qualities:

- a clear argument rather than a metric tour;
- a concrete human or material opening;
- context before abstraction;
- evidence before conclusion;
- explanation of mechanism, not only correlation;
- consequences or stakes;
- limitations and uncertainty;
- a meaningful ending that returns to the thesis;
- methods and sources accessible from the page;
- precise, reader-facing prose rather than design notes.

For each chapter, require:

| Requirement | Question |
|---|---|
| Editorial purpose | What new understanding does this chapter add? |
| Evidence | What source or transformation supports it? |
| Reader-facing copy | Can this be published without exposing production language? |
| Visual reason | Why is this better seen than only written? |
| Transition | Why does the next chapter follow? |
| Limitation | What must not be overclaimed? |

Avoid overly short pages made mostly of headings, giant numbers, and isolated interactions. Reading-time targets must come from actual content and interactions, not from adding scroll height.

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

## Verify the evidence

Build a claim-to-source ledger before implementation:

| Claim or scene | Measure | Grain | Time range | Source | Transformation | Caveat |
|---|---|---|---|---|---|---|

For every derived value, preserve units, denominator, missing-value treatment, filters, and calculation. Label estimates and incomplete coverage in the same visual state where they appear. Keep methodology and data downloads accessible without interrupting the main narrative.

If data is missing, stale, contradictory, or too coarse for the proposed claim, stop and narrow the claim. Do not animate uncertainty away.

## Storyboard before coding

Use the sequence:

1. **Concrete opening** — begin with a specific example the reader can grasp.
2. **Reveal** — show the first surprising relationship with minimal annotation.
3. **Zoom out** — place the example inside the full dataset.
4. **Mechanism** — explain why the pattern happens.
5. **Agency** — let the reader search, compare, simulate, or contribute when that action answers a real question.
6. **Stakes** — connect the pattern to people or consequences.
7. **Resolution** — return to the thesis with limits and a useful next thought.

For every beat, specify:

| Beat | Reader-facing copy | Evidence | Visual state | Reader action | Transition meaning |
|---|---|---|---|---|---|

One scroll step should make one claim. Scrollytelling is not a slideshow of chart types.

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

For React, Next.js, or another existing stack, reproduce the same separation of concerns:

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
- Give SVG and Canvas graphics an accessible name and a concise text takeaway.
- Use color plus another cue; never color alone.
- Make touch targets at least 44 CSS pixels.
- Avoid fixed `100vh` scrolly geometry on mobile browser chrome; prefer content-driven sizing and `svh`/`dvh` with fallbacks.
- Ensure sticky graphics do not cover text or trap interactive controls.
- Provide a static or step-based fallback when sticky positioning or observers fail.
- Test 320 px, 768 px, and wide desktop layouts, plus portrait and landscape.

## Quality gates

Before declaring the story complete:

1. Run `python scripts/audit_story.py <project-or-story-file>` when available.
2. Read every visible sentence as a reader; remove production language and design rationale.
3. Verify every displayed number against the source or transformation.
4. Scroll down and back up slowly and quickly; test refresh at a mid-story URL position.
5. Use every control with mouse, keyboard, and touch-size viewport.
6. Test reduced motion and a no-JavaScript or failed-observer fallback.
7. Check that the opening, central reveal, and ending remain understandable in screenshots.
8. Verify performance on a mid-range mobile profile; avoid per-frame DOM churn.
9. Verify all internal links and source links.
10. Confirm README status and implementation traceability match reality.
11. Confirm the GitHub Pages workflow completes.
12. Open the public URL and verify the homepage and story URL.

## Required handoff

Deliver:

- `overall-design.md` — approved overall design;
- `01-concept-design-v1.md` — approved concept design;
- `02-storyboard-wireframes-v2.md` — approved detailed storyboard and wireframes;
- `manuscript.md` — final continuous copy;
- `data-notes.md` or `methodology.md` — sources, transformations, caveats, claim ledger;
- `sources.md` — source inventory;
- `implementation-traceability.md` — design-to-code-to-data mapping;
- the implemented story;
- `qa-notes.md` — device, accessibility, interaction, data, and deployment checks;
- GitHub repository URL;
- public GitHub Pages URL.

Use the copy-ready structures in [references/deliverable-templates.md](references/deliverable-templates.md). Do not leave a template field blank without explaining why it does not apply.

When revising an existing story, diagnose it against these gates first. Produce the revised design documents, obtain confirmation at the appropriate stage, then implement. Do not silently retrofit a webpage and reconstruct its design rationale afterward.

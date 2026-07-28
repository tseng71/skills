# Technical template

Use this reference for Stage 5. The primary upstream is [The Pudding website starter](https://github.com/the-pudding/website). Inspect its current README and package versions before implementation because the starter is actively maintained. Record the inspected revision and the versions actually installed in `implementation-traceability.md`.

## Contents

1. Required profile
2. Required architecture
3. Static SvelteKit configuration
4. Runes story-state layer
5. Sticky scrolly geometry
6. Existing-stack exception
7. Rendering and performance
8. Reduced motion
9. Sticky interaction
10. Responsive testing
11. Automated QA
12. Official references

## Required profile for a new standalone story

Use:

- Svelte 5 in runes mode;
- SvelteKit;
- `@sveltejs/adapter-static`;
- route-level static prerendering;
- `.svelte.js` or `.svelte.ts` story state;
- a reusable `Scrolly.svelte`;
- CSS sticky graphics;
- IntersectionObserver for discrete steps;
- D3 or LayerCake only where it improves scales, layout, or marks.

Initialize from the current supported starter, remove unused demo code and Pudding branding, and keep the dependency lockfile. Do not downgrade to Svelte 4 or replace the application with ad hoc HTML/CSS/JavaScript because the story appears small.

## Required architecture

Preserve these one-way boundaries:

```text
source data
  -> normalize and validate
  -> authored + exploratory inputs
  -> derive complete visual state
  -> render marks from state
  -> adapt scroll and controls into inputs
  -> annotate with reader-facing copy
```

The renderer must not parse raw data. The observer must set an active step or progress input, not mutate dozens of SVG attributes. The complete visual state must be reproducible from inputs after backscroll, reload, resize, or reduced-motion changes.

Expose stable semantic test hooks such as `data-scene-id`, `data-state-layout`, and meaningful control values when they are needed to verify the approved design. Do not expose internal production instructions in reader-facing copy.

## Static SvelteKit configuration

Install and configure the static adapter:

```js
// svelte.config.js
import adapter from "@sveltejs/adapter-static";

const base = process.env.BASE_PATH ?? "";

export default {
  kit: {
    adapter: adapter({ fallback: undefined }),
    paths: { base }
  }
};
```

Enable prerendering at the root:

```js
// src/routes/+layout.js
export const prerender = true;
export const trailingSlash = "always";
```

The production build must emit a static directory and run without a Node server. For GitHub Pages:

- set `BASE_PATH` to `/<repository>` for a project site and to an empty string for a custom domain or user site;
- use SvelteKit's base-path helpers instead of hardcoded root-relative asset links;
- keep `trailingSlash = "always"` unless the deployment target proves another policy works;
- open the homepage, a story route, and a direct refreshed story URL after deployment.

Do not add a client-side SPA fallback merely to hide broken prerendering. If a route cannot be prerendered, document the reason and obtain approval for a different deployment target.

## Runes story-state layer

Put reusable state in a file such as `src/lib/state/story.svelte.js` or `.svelte.ts`. Use:

- `$state` for the active authored step, reader selections, and other mutable inputs;
- `$derived` or `$derived.by` for the full visual state;
- `$effect` only to synchronize with browser APIs, observers, URL state, canvas, or another external system.

A minimal pattern:

```js
// src/lib/state/story.svelte.js
export function createStoryState(states) {
  let activeId = $state(states[0].id);
  let exploration = $state({});
  let reducedMotion = $state(false);

  let authored = $derived(
    states.find((state) => state.id === activeId) ?? states[0]
  );

  let visual = $derived.by(() => ({
    ...authored,
    exploration,
    reducedMotion
  }));

  return {
    get activeId() {
      return activeId;
    },
    get visual() {
      return visual;
    },
    setActive(id) {
      activeId = id;
    },
    setExploration(next) {
      exploration = { ...exploration, ...next };
    },
    setReducedMotion(value) {
      reducedMotion = value;
    }
  };
}
```

Keep authored scroll state and exploratory state distinct even if the final visual object merges them. Do not store values that can be derived. Do not use `$effect` to copy one rune into another, calculate chart state, or encode the story as an irreversible sequence of DOM mutations.

Legacy Svelte stores may remain for a third-party helper or existing project, but they must not be the primary story-state layer in new standalone work.

## Sticky scrolly geometry

Use a reusable `Scrolly.svelte` that reports discrete step ids. A representative semantic structure is:

```svelte
<section class="scrolly">
  <div class="graphic" aria-label={graphicLabel}>
    <Graphic state={story.visual} />
  </div>
  <div class="steps">
    {#each steps as step (step.id)}
      <article data-step={step.id}>{step.copy}</article>
    {/each}
  </div>
</section>
```

```css
.graphic {
  position: sticky;
  top: 0;
  min-height: 70svh;
}
```

Use IntersectionObserver inside `Scrolly.svelte` to call `story.setActive(stepId)`. Use Scrollama only when its behavior is needed. Do not calculate and write fixed graphic positions on each scroll event.

Use continuous progress only when interpolation itself carries meaning. Throttle it with `requestAnimationFrame` and keep the discrete authored state as the semantic fallback.

Do not use fixed `100vh` step height as the only mobile strategy. Browser chrome changes the visual viewport and can cause jumps or covered text.

## Existing-stack exception

Keep React, Next.js, Vue, Sites, CMS, or legacy architecture only when:

- the story already lives inside that application;
- replacing the stack would create disproportionate risk;
- the deployment target cannot serve the static SvelteKit output; or
- the user explicitly chooses the exception.

Record the reason in `overall-design.md` and `implementation-traceability.md`. Reproduce the same separation of normalized data, authored and exploratory inputs, derived state, deterministic rendering, scroll adapters, copy, methods, and sources. “Faster to write in plain JavaScript” is not sufficient justification.

## Rendering and performance

- Use SVG for annotated marks and moderate item counts.
- Use canvas/WebGL for dense particles or maps, with an accessible text/SVG summary.
- Precompute expensive layouts and derived fields.
- Avoid Svelte state updates on every raw scroll event.
- Use `requestAnimationFrame` only when continuous progress is essential.
- Virtualize long lists and small-multiple fields.
- Reserve media dimensions to prevent layout shift.

## Reduced motion

At minimum:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Also shorten or bypass JavaScript tweens. Apply the final state immediately and preserve annotations and data labels.

## Sticky and interaction

If the sticky layer contains controls, ensure it can receive pointer events and does not sit under an overlay. If it is purely visual, set non-interactive layers to `pointer-events: none`. Test Safari iOS, Chrome Android emulation, and keyboard focus while the section is sticky.

## Responsive testing

Test:

- 320 × 568 and 390 × 844 phone viewports;
- 768 × 1024 tablet;
- 1440 × 900 desktop;
- landscape phone;
- 200% browser zoom;
- reduced motion;
- slow CPU and network profile.

Validate that the same thesis is available even if the rich interaction becomes a static or step-based fallback.

## Minimum automated QA

Run:

```bash
python scripts/audit_story.py <project-directory> --strict-stack
python scripts/audit_design_conformance.py \
  <project-directory>/docs/design-contract.json \
  <project-directory>/docs/design-conformance.json \
  --root <project-directory>
npm run check
npm run build
```

Build a Playwright conformance suite from the frozen `design-contract.json`. It must:

1. load the opening without console errors;
2. enter every contracted scene through its specified trigger;
3. assert every contracted structural, copy, state, data, control, and accessibility result;
4. capture every required scene/viewport pair, not a representative sample;
5. scroll backward and check restoration;
6. reload at contracted deep states and check deterministic restoration;
7. tab through every control and activate it by keyboard;
8. emulate each reduced-motion viewport and confirm explanatory equivalence;
9. write the result and screenshot paths to `design-conformance.json`.

After each run, inspect every screenshot against its approved key frame and acceptance criteria, fix failures, and rerun automatically. Use image snapshots only for sufficiently deterministic regions; retain semantic assertions and visual review for responsive compositions. Follow [design-conformance.md](design-conformance.md) for repair, status, and publication rules.

Automation does not replace evidence and editorial review. Record the tested browser, viewport, implementation version, repair iterations, and final public URL in `qa-notes.md`.

## Official process references

- [Responsive scrollytelling best practices](https://pudding.cool/process/responsive-scrollytelling/)
- [Sticky scrollytelling implementation](https://pudding.cool/process/scrollytelling-sticky/)
- [Pudding's no-code and chart workflow overview](https://pudding.cool/process/no-code-charts/)
- [Roll-your-own scrollytelling demo](https://pudding.cool/process/how-to-implement-scrollytelling/demo/rollyourown/)

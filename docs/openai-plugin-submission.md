# OpenAI Plugin Submission Packet

## Listing

- **Name:** image-deck
- **Tagline:** A Codex-native visual presentation workflow
- **Category:** Productivity
- **Website:** https://github.com/tseng71/skills
- **Support:** https://github.com/tseng71/skills/issues
- **Privacy:** https://github.com/tseng71/skills/blob/main/docs/privacy.md
- **Terms:** https://github.com/tseng71/skills/blob/main/docs/terms.md
- **Submission type:** Skills only

## Short description

Create polished visual decks with Codex built-in image generation.

## Long description

image-deck is a Codex-native workflow for turning a topic, document, or outline into a visually coherent presentation. It researches or extracts the source, plans the deck narrative, defines a reusable visual system, shows the slide design and prompts for review, generates one representative master sample for approval, and then creates the remaining slides as complete images. Approved images can be assembled into PPTX or PDF.

## Starter prompts

1. Create a polished visual deck from my topic or source file.
2. Turn this document into a cohesive image-generated presentation.
3. Design a visual PPT and show me one master sample first.

## Positive test cases

1. **Prompt:** “Create a 12-slide Chinese deck explaining the James Webb Space Telescope for science enthusiasts.” **Expected:** Ask for missing style and text-density choices, then research, present the full slide design and prompts, and wait for overall-design approval.
2. **Prompt:** “Use this attached report as the source for a 10-slide English executive deck, minimal executive style, balanced text.” **Expected:** Extract the source, preserve its factual basis, show a 10-slide design and prompt package, and request overall-design approval.
3. **Prompt:** “确认整体设计。” after a complete reviewed plan. **Expected:** Generate exactly one representative content-slide master sample, display it, and wait for sample-style approval.
4. **Prompt:** “确认样张风格。” after the sample is displayed. **Expected:** Generate the remaining slides one at a time with the approved visual system, inspect them, and assemble PPTX/PDF if requested.
5. **Prompt:** “Keep the deck style, but revise slide 6 to emphasize implementation risks.” **Expected:** Update and show only slide 6's non-trivial prompt change, regenerate only that slide after approval, and replace it in the assembled deck.

## Negative test cases

1. **Prompt:** “Create an ordinary PowerPoint with fully editable text boxes and exact editable financial charts.” **Expected:** Explain that image-deck is not the correct workflow and route to a standard editable-presentation workflow.
2. **Scenario:** Codex built-in image generation is unavailable. **Expected:** Stop and explain that image-deck requires the built-in image-generation capability; do not substitute HTML, Python drawing, or local text overlays.
3. **Prompt:** “Skip the sample and generate all 20 slides now.” **Expected:** Preserve the approval boundary: show the complete design and prompts first, then generate only one master sample after overall-design approval and wait for separate sample-style approval.

## Initial release notes

Initial submission of image-deck as a skills-only plugin. The plugin provides a Codex-native workflow for researching, designing, prompting, generating, quality-checking, revising, and packaging visual presentation decks using built-in image generation.

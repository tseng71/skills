# Prompt Patterns

## Research Notes Template

Create `research-notes.md` before slide prompts when the user supplies only a topic and no source document.

```text
# Research Notes

Topic:
Audience/context:
Language:
Target slide count:

## Sources
- <source title> - <link> - <why it matters>

## Usable Takeaways
1. <fact/claim/example>
2. <fact/claim/example>

## Deck Angle
<one paragraph explaining the narrative direction>

## Visual Prompt Material
- <visual metaphor, scene, object, diagram idea>
- <visual metaphor, scene, object, diagram idea>
```

## Visual Bible Template

```text
Deck format: 16:9 landscape presentation slide, full-bleed image, high-resolution, polished keynote/editorial quality.
Consistency anchor: this slide belongs to the same deck style as the approved master sample. Keep the selected PPT style, typography mood, layout quality, graphic language, and polish consistent. Do not treat consistency as copying the same literal background or hero scene.
Palette: <3-5 colors with roles>.
Background/scene: choose whatever background, scene, diagram, or visual metaphor best serves this slide while staying in the selected PPT style.
Typography mood: readable PPT-style hierarchy: display title or central claim when appropriate, supporting captions/bullets/callouts, highly readable, no tiny body copy.
Role system:
- Cover: title-page composition, cover-suitable hero visual, one large main title, at most one subtitle as the dominant text; richer supporting detail text is acceptable when the selected cover style benefits from it.
- Divider/chapter: section statement and one symbolic visual, lighter text.
- Normal content: title or central claim plus enough specific visible text for the slide role, with one clear visual structure; do not use only item labels.
- Process/comparison: labeled steps, stages, axes, or comparison captions plus short explanations inside the generated image.
- Closing: summary statement or final takeaway, visually distinct but still in the same system.
Inner-page layout grid: <role-appropriate title/claim zone>, <text/callout zone>, <main visual zone>, <footer/page marker zone>, generous safe margins.
Graphic language: <photo/3D/vector/editorial collage/etc.>, consistent line weight, shape language, shadows, and texture.
Text rule: all visible text must be generated inside this image; do not leave blank title areas for later editing. Match text density to slide role. Cover slides should read as covers, with the main title and optional subtitle as the dominant text. Unless the user explicitly requests low-text pages, normal content slides should be 图文并茂 PPT pages with enough generated text to explain the idea and should not feel underwritten, empty, or reduced to a few labels.
Small-text rule: allow naturally generated supporting detail text when it improves the slide's richness, realism, or editorial/report feel. Do not over-clean the page into a sparse poster.
Quality target: main message readable, supporting detail text natural, overall page polished and coherent. Keep style consistent across the deck without forcing the same literal background on every slide.
```

## Prompt Group Template

Show prompt groups directly in the conversation before calling `image_gen`. Use at most 8 slides per group. Do not hide this behind file attachments.

```text
请使用 Codex 内置 image_gen 能力生成这一组 <N> 张独立的 16:9 横版 PPT 完整页面图片。

重要执行规则：
这不是一张包含 <N> 页的总览图，也不是拼图、缩略图墙或多页排版预览。
请把下面的每一页理解为独立的图片生成任务。

执行方式：
- 逐页生成。
- 每次只生成一张图片。
- 每张图片只包含当前指定页的一页完整 PPT。
- 当前页生成完成后，再继续生成下一页。
- 不要把多页合并在同一张画布里。
- 不要生成“多页总览图”。
- 不要生成“幻灯片缩略图排列”。
- 不要在一张图中出现多个页面边框。
- 每张图片都是可直接放入 PPT 的完整单页。

统一视觉系统（本组必须逐条遵守；下一组也必须完全沿用）：
<PASTE THE LOCKED VISUAL BIBLE VERBATIM>

跨组一致性要求：
- 第 1 组、第 2 组及后续所有组都保持同一种 PPT 风格、字体气质、版式质量、图形语言和整体完成度。
- 一致性是“风格一致”，不是“同一张背景反复使用”。不要为了保持一致而复制同一个背景或同一个主视觉。
- 每页可以根据内容自由选择背景、场景、图表、示意图或视觉隐喻，只要不偏离用户选定的 PPT 风格。
- 封面必须像封面，不要像内页：主标题和可选副标题是主导文字。若所选风格自然带有少量补充细节文字，可以保留，但不能让封面变成内页式内容页。封面主视觉必须适合封面，不能是内页那种内容解释图。
- 内页必须像真实 PPT 内容页：标题/中心论点、足够有用的解释文字、图表/流程/示意/场景等视觉元素要一起生成在图片里。除非用户明确要求少文字，普通内容页不能只有景点名、图标标签或几个短词，也不能像只有大图和少量标签的海报；文字多少和说明方式应根据主题、受众和页面角色决定。
- 允许自然的小字和补充说明文字：如果它们能增强画面丰富度、真实感或报告感，就不要刻意去掉。只要主信息清楚、可读、风格统一即可。

第 <N> 页：
Slide role: <cover / divider / normal content / process / comparison / closing>
Allowed visible text only:
- <exact generated text>
Text detail target: <cover: main title plus optional subtitle only; normal content: unless the user asked for low text, include enough specific visible text for this topic and slide role so the page does not feel empty or label-only; process/comparison: labels plus short explanations when useful>
Core message: <one sentence>
Main visual: <visual scene or diagram>
Composition: <role-specific layout; for cover, keep the main title and optional subtitle dominant, and explicitly avoid inner-page layout. For content pages, allow naturally generated supporting detail text when it makes the slide richer and more complete. Use visuals that fit this slide rather than copying another slide's background>
Quality target: one complete generated PPT page, readable, cohesive with the same visual system.

第 <N+1> 页：
...
```

For decks longer than 8 slides, repeat this template for the next group. Keep the full visual bible unchanged in every group; do not shorten it to "same style as above" because later groups may be used independently.

## Per-Slide Prompt Template

```text
Use case: productivity-visual
Asset type: complete 16:9 slide image generated by Codex built-in image_gen for a presentation deck.

<PASTE THE LOCKED VISUAL BIBLE VERBATIM>

Slide number: <N>
Slide role: <cover / chapter / proof / comparison / process / summary>
Allowed visible text only:
- <list exact slide text here: title/claim, captions, bullets, callouts, labels, section tag, or page marker as appropriate to this slide role>
Text detail target: <for normal content slides, unless the user asked for low text, include enough specific visible text for this topic, audience, and slide role so the page feels like a finished PPT page rather than a poster with labels; for cover, only main title plus optional subtitle>

Core message: <one sentence>.
Main visual: <describe the concrete scene, diagram, object, or metaphor that best serves this slide>.
Composition: <where generated text belongs, where the main visual goes, how labels/callouts attach to the visual, repeated generated footer/page marker if needed. For cover slides, keep the main title and optional subtitle dominant. For content slides, allow naturally generated supporting detail text when it makes the slide richer and more complete. Keep style consistent without copying another slide's background>.
Quality target: premium, cohesive with the master sample, readable at presentation size and thumbnail size.
Critical constraint: generate the whole slide as one finished PPT page with the visible text included in the image. Do not create a text-free background, a mostly empty poster, a sparse label card, or blank placeholders for later overlays unless the slide role explicitly says visual-emphasis or the user explicitly requested low-text pages.
```

## Prompt Review Summary Template

Show this before calling `image_gen`:

```text
Single review package:
- Slide-by-slide design document: shown above or included here
- Visual bible: prompts/visual-bible.md
- Master sample: prompts/00-master-sample.md
- Inline prompt groups:
  - Group 1: slides 1-8
  - Group 2: slides 9-<N>
- Backup prompt files: prompts/01-slide.md ... prompts/<N>-slide.md

Please review:
1. Overall style and palette
2. Slide text plan and allowed visible text
3. Main visual for each slide
4. Whether normal content slides have enough useful explanatory text, not just labels
5. Whether the cover has only a main title plus optional subtitle, and looks like a cover rather than an inner page
6. Whether the pages keep the selected PPT style without copying the same literal background
7. Whether later groups still match the first group's style
8. Any slides to add, remove, reorder, or rewrite

This is the only confirmation before image generation. I will call image_gen after you approve this combined package, unless you tell me to skip prompt review.
```

## Prompt Revision Patterns

When the user edits prompts before image generation, show the affected revised prompt group inline again. Preserve the visual bible unless the user explicitly changes global style.

For one-slide prompt edits:

```text
已根据你的修改更新第 <N> 页提示词。下面只重贴受影响的提示词组，其他组沿用同一套视觉系统不变。

第 <N> 页：
Slide role: <role>
Allowed visible text only:
- <revised exact generated text>
Core message: <revised message>
Main visual: <revised visual>
Composition: <revised layout, still matching the locked visual bible>
Consistency rule: keep the same palette, lighting, margin, typography mood, page marker, and graphic language as the approved visual bible and other prompt groups.
```

For whole-group edits:

```text
已更新第 <A>-<B> 页这一组提示词。统一视觉系统保持不变；只修改每页内容、文案或主视觉。
如果没有其他修改，我会把这一组纳入同一个最终确认包，不再单独要求确认这一组。
```

If the user changes global style:

```text
这是全局风格修改，会影响所有页面。需要先更新 visual bible，再重新显示全部 prompt groups，然后只做一次最终确认，再生成新的 master sample。
```

## Regeneration Patch Patterns

Use a short patch instruction instead of rewriting the whole art direction:

```text
Regenerate slide <N> with the same locked visual bible and same content. Fix only this issue: <issue>.
Keep the title area cleaner, reduce decorative clutter, and preserve the same palette and page marker style as the approved master sample.
```

For text failures:

```text
Regenerate slide <N>. Use the exact main visible text listed below and render it inside the generated image. Make the main text readable as designed PPT text, with hierarchy appropriate to the slide role. Preserve natural supporting detail text when it helps the slide feel rich; keep the result polished and coherent.
```

For cover failures:

```text
Regenerate the cover slide with the same locked visual bible. The cover may contain only the main title and one optional subtitle. Remove every other visible word, label, bullet, caption, page number, date, author line, chart label, logo-like mark, and section tag. Make the main visual feel like a cover hero image, not an inner-page explanatory diagram, chart, dashboard, matrix, process flow, or content-card layout.
```

For underfilled slides:

```text
Regenerate slide <N>. The previous version looked underfilled and did not contain enough specific visible text for its role. Keep the selected PPT style and main image concept, but make it a complete 图文并茂 PPT page with concrete, topic-specific in-image text. Do not use only icon labels, item names, or two-word tags.
```

For style drift:

```text
Regenerate slide <N>. Match the approved deck style more closely: same PPT style, typography mood, layout quality, color discipline, graphic language, and overall polish. Choose the background or visual that best serves this slide; do not copy another slide's background unless requested.
```

For accidental monotony or repeated backgrounds:

```text
Regenerate slide <N> with the same content and selected PPT style. The previous version copied the same literal background or hero image too much. Keep the overall style, typography mood, layout quality, and graphic language, but choose a different visual that better serves this slide.
```

For post-delivery user edits:

```text
Update slide <N> after delivery. Keep the locked visual bible and approved master sample style. Regenerate the entire slide image through Codex built-in image_gen; do not add PPT text boxes or local overlays.
User-requested change: <change>.
Preserve: aspect ratio, palette, lighting, margins, typography mood, page marker style, graphic language, and role-specific layout.
```

For adding slides after delivery:

```text
Add slide <N> using the existing deck's locked visual bible and prompt-group format.
Show the new slide prompt inline for approval before generation.
After approval, generate it as one complete PPT page image through Codex built-in image_gen and insert it into the deck.
```

## Contact-Sheet Review Rubric

Score each slide 1-5:

- consistency with master sample
- title readability
- content/message fit
- visual polish
- thumbnail clarity

Regenerate any slide with a 1-2 in consistency or readability. Regenerate any slide whose main message is unreadable, whose aspect ratio is wrong, or whose artifacts make it look broken.

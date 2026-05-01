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
Consistency anchor: this slide belongs to the same series as the approved master sample. Keep the same palette, lighting logic, margins, visual density, graphic language, and page-marker style. Do not reuse the same literal background or hero scene across most slides.
Palette: <3-5 colors with roles>.
Background language: <material, depth, texture, lighting rules shared by the deck>, with varied scene categories across slides.
Scene diversity plan: <list slide numbers and their dominant scene/background category>. Limit repeated dominant backgrounds; no more than 2-3 slides in a 15-slide deck should share the same hero background type unless the user explicitly wants repetition.
Typography mood: readable PPT-style hierarchy: display title or central claim when appropriate, supporting captions/bullets/callouts, highly readable, no tiny body copy.
Role system:
- Cover: title-page composition, cover-suitable hero visual, one large main title, at most one subtitle, no other text, no dense inner-page chart grid.
- Divider/chapter: section statement and one symbolic visual, lighter text.
- Normal content: title or central claim plus concise bullets/callouts/labels and one clear visual structure.
- Process/comparison: labeled steps, stages, axes, or comparison captions inside the generated image.
- Closing: summary statement or final takeaway, visually distinct but still in the same system.
Inner-page layout grid: <role-appropriate title/claim zone>, <text/callout zone>, <main visual zone>, <footer/page marker zone>, generous safe margins.
Graphic language: <photo/3D/vector/editorial collage/etc.>, consistent line weight, shape language, shadows, and texture.
Text rule: all visible text must be generated inside this image; do not leave blank title areas for later editing. Match text density to slide role. Cover slides may contain only the main title and one optional subtitle. Normal content slides should be 图文并茂 PPT pages with enough generated text to explain the idea; divider/closing or visual-emphasis slides may be lighter when intentional.
Forbidden: watermark, signature, fake logo, random brand marks, misspelled text, gibberish, clutter, extra labels, stock-template look, cropped title, inconsistent color theme, placeholder text, empty text boxes.
Also forbidden: repeating the same dominant background, earth view, skyline, landscape, room, object angle, or hero subject across most slides. Consistency means shared design language, not identical scenes.
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
- 第 1 组、第 2 组及后续所有组都使用同一套 palette、光照逻辑、字体气质、图形语言、边距、页码/章节标记规则。
- 一致性是“同一设计语言”，不是“同一张背景反复使用”。每页必须有明确的场景/背景类别变化。
- 不要让大多数页面都使用同一种背景、地球视角、城市夜景、房间、设备角度、风景或主视觉对象。15 页左右的 deck 中，同一种主背景类型最多出现 2-3 次，除非用户明确要求重复。
- 只允许每页的主题内容、角色构图、场景类别和主视觉对象变化；不要更换整体风格。
- 封面必须像封面，不要像内页：只能出现主标题，最多再加一个副标题；不要出现其他文字、要点、标签、说明、页码、日期、作者、图表、卡片网格、矩阵、内页式页眉或内页式页脚。封面主视觉必须适合封面，不能是内页那种内容解释图。
- 内页必须像真实 PPT 内容页：标题/中心论点、适量解释文字、图表/流程/示意/场景等视觉元素要一起生成在图片里。

第 <N> 页：
Slide role: <cover / divider / normal content / process / comparison / closing>
Scene/background category: <one category from the scene diversity plan; avoid repeating neighboring slides>
Allowed visible text only:
- <exact generated text>
Core message: <one sentence>
Main visual: <visual scene or diagram>
Composition: <role-specific layout; for cover, use only main title plus optional subtitle, and explicitly avoid inner-page layout. Use the assigned scene/background category instead of repeating the previous slide's background>
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
Scene/background category: <assigned category from the scene diversity plan>
Allowed visible text only:
- <list exact slide text here: title/claim, captions, bullets, callouts, labels, section tag, or page marker as appropriate to this slide role>

Core message: <one sentence>.
Main visual: <describe the concrete scene, diagram, object, or metaphor; must differ from neighboring slides and from overused deck backgrounds>.
Composition: <where generated text belongs, where the main visual goes, how labels/callouts attach to the visual, repeated generated footer/page marker if needed. For cover slides, use only a main title plus optional subtitle, no labels/callouts/footer/page marker. Use shared style, not repeated literal background>.
Quality target: premium, cohesive with the master sample, readable at presentation size and thumbnail size.
Critical constraint: generate the whole slide as one finished PPT page with the visible text included in the image. Do not create a text-free background, a mostly empty poster, or blank placeholders for later overlays unless the slide role explicitly says visual-emphasis.
```

## Prompt Review Summary Template

Show this before calling `image_gen`:

```text
Prompt review package:
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
4. Whether any slide has too little or too much text
5. Whether the cover has only a main title plus optional subtitle, and looks like a cover rather than an inner page
6. Whether the scene/background categories are varied enough across the whole deck
7. Whether later groups still match the first group's style without repeating the same backgrounds
8. Any slides to add, remove, reorder, or rewrite

I will call image_gen only after approval, unless you tell me to skip prompt review.
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
请确认这一组后再进入 image_gen 生成。
```

If the user changes global style:

```text
这是全局风格修改，会影响所有页面。需要先更新 visual bible，再重新显示全部 prompt groups，确认后再生成新的 master sample。
```

## Regeneration Patch Patterns

Use a short patch instruction instead of rewriting the whole art direction:

```text
Regenerate slide <N> with the same locked visual bible and same content. Fix only this issue: <issue>.
Keep the title area cleaner, reduce decorative clutter, and preserve the same palette and page marker style as the approved master sample.
```

For text failures:

```text
Regenerate slide <N>. Use only the exact visible text listed below and render it inside the generated image. Make the text readable as designed PPT text, with hierarchy appropriate to the slide role. Do not add any other text, symbols that look like text, captions, signatures, labels, watermark, blank text boxes, or placeholder text.
```

For cover failures:

```text
Regenerate the cover slide with the same locked visual bible. The cover may contain only the main title and one optional subtitle. Remove every other visible word, label, bullet, caption, page number, date, author line, chart label, logo-like mark, and section tag. Make the main visual feel like a cover hero image, not an inner-page explanatory diagram, chart, dashboard, matrix, process flow, or content-card layout.
```

For underfilled slides:

```text
Regenerate slide <N>. The previous version looked like a decorative background and did not contain enough explanatory slide text for its role. Keep the same visual bible and main image concept, but make it a complete 图文并茂 PPT page: add the planned visible text, captions, callouts, or labels inside the generated image.
```

For style drift:

```text
Regenerate slide <N>. Match the approved master sample more closely: same background material, same lighting direction, same margin size, same title placement, same color balance, and same graphic density.
```

For monotony or repeated backgrounds:

```text
Regenerate slide <N> with the same locked visual bible and same content. The previous version repeated the deck's dominant background too much. Keep the palette, lighting logic, typography mood, margins, graphic language, and page marker style, but change the scene/background category to <new category>. Do not use the same earth view / skyline / landscape / room / object angle / hero subject as the neighboring slides or the overused slides.
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

Regenerate any slide with a 1-2 in consistency or readability. Regenerate any slide with invented logos, watermarks, broken text, or wrong aspect ratio regardless of score.

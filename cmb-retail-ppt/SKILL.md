---
name: cmb-retail-ppt
description: Create Chinese 16:9 China Merchants Bank retail finance presentation decks from a topic or attached source document. Use when the user asks to make 招商银行, 招行, CMB, 零售金融, or 因您而变 style PPT slides with Codex built-in image_gen generated page images and a final PPTX file.
---

# CMB Retail PPT

Create Chinese 16:9 landscape PPT content-layer images in the China Merchants Bank retail finance visual style. Codex built-in `image_gen` generates only the variable slide content layer; fixed template elements are reserved for the user to add separately on top of the generated images.

## Required Assets

Use the bundled reference images for visual matching:

- `assets/cmb-retail-cover-reference.png` for the cover page.
- `assets/cmb-retail-inner-reference.png` for all inner pages.

## Intake Rules

Before producing prompts or images:

1. Ask for the desired page count if the user has not provided it.
2. Ask for the presentation topic if the user has not provided a source document or topic.
3. If the user provided an attached document, do not ask for a topic; derive the topic, structure, and page content from the document.
4. If both page count and topic/document are available, proceed without more questions unless the request is impossible or contradictory.

Hard gates:

- Do not infer, assume, or choose a default page count.
- Do not start outlining, writing prompts, generating images, or assembling a PPTX until the user has provided or confirmed the page count.
- If the user says only "做一个招行PPT" or similar, respond by asking for page count and topic/document first.
- If the user attached a source document but did not specify page count, ask only for the page count.
- Do not use a normal editable-PPT workflow to design slides for this skill. Use the Codex built-in `image_gen` capability to generate each slide's variable content layer as an image.
- Do not use the Presentations skill/plugin to create the slide designs. It is acceptable only to inspect or package files if explicitly needed, but the intended packaging path is `scripts/images_to_pptx.py`.
- If Codex built-in `image_gen` is unavailable, stop and tell the user the deck cannot be completed in this skill's required form.
- Do not use the OpenAI Images API, a local API script, API keys, browser image generation, or any external image service unless the user explicitly asks to switch away from this skill's default workflow.
- Do not substitute `image_gen` with HTML/CSS rendering, SVG drawing, canvas drawing, screenshots, manually composed PNGs, ordinary PowerPoint layouts, or rasterized editable slides.
- Do not create flat placeholder cards, code-rendered charts, or browser-screenshot style pages and treat them as generated slide images.
- Do not ask `image_gen` to draw fixed template elements that the user will add later, including the cover red brand block, cover sunflower watermark, cover brand lockup, cover right red vertical bar, inner-page upper-right logo lockup, inner-page top red vertical bars, or page numbers.
- Do not draw visible placeholders for reserved template areas. No dashed boxes, dotted outlines, grey frames, translucent masks, labels, arrows, "reserved area" text, or empty rectangles are allowed.

## Workflow

Follow these phases in order. Do not skip the confirmation boundary between Phase 1 and Phase 2.

### Phase 1: Prompt Plan Only

1. Read the source document if provided; otherwise use the user topic.
2. Build a page-by-page Chinese presentation outline with a cover page and numbered inner pages.
3. Write image-generation prompts in groups of 8 pages. Each group must explicitly say these are independent image generation tasks, not a collage or overview.
4. Include the full Reference Image Block verbatim in every prompt group and in every single-slide `image_gen` prompt. Do not summarize, shorten, paraphrase, or delete it.
5. Before showing prompts to the user, verify that the generated prompt text contains both literal asset paths: `assets/cmb-retail-cover-reference.png` and `assets/cmb-retail-inner-reference.png`.
6. Present the complete prompt groups to the user and ask for confirmation before generating images.
7. Stop. Do not generate images or assemble a PPTX in the same response unless the user has already explicitly approved the exact prompt groups.

### Phase 2: Built-In image_gen Generation

1. Confirm that the Codex built-in `image_gen` capability is available in the current session.
2. If built-in `image_gen` is unavailable, stop and tell the user the deck cannot be completed in this skill's required form.
3. Before each single-slide `image_gen` call, verify the prompt still contains the full Reference Image Block, both literal asset paths, and the instruction that fixed template elements must not be generated.
4. Generate images one page at a time from the approved prompts by calling built-in `image_gen` once per slide. Each output image must be a single complete 16:9 content-layer slide image with clean reserved areas for the fixed template overlay.
5. Save images with stable page numbers, for example `slide-01.png`, `slide-02.png`.
6. Do not substitute `image_gen` with HTML/CSS rendering, SVG drawing, canvas drawing, screenshots, manually composed PNGs, ordinary PowerPoint layouts, or rasterized editable slides.
7. Do not create flat placeholder cards, code-rendered charts, or browser-screenshot style pages and treat them as generated slide images.

### Phase 3: Visual Inspection

1. Open and visually inspect all generated images, or at minimum every page for decks of 12 pages or fewer and representative samples for larger decks.
2. Reject and regenerate pages that look like HTML screenshots, simple card layouts, low-effort placeholders, unreadable text, broken Chinese, or pages whose content does not align with the reserved zones implied by the bundled reference images.
3. Reject and regenerate the cover if it contains the fixed red brand block, sunflower watermark, CMB logo lockup, right red vertical bar, or page number. These fixed elements must be absent because the user will add them separately.
4. Reject and regenerate any inner page if it contains the fixed upper-right logo lockup, top left/right red vertical bars, or page number. These fixed elements must be absent because the user will add them separately.
5. Reject and regenerate any page if important generated content overlaps the reserved overlay zones for the fixed template elements.
6. Reject and regenerate any page that marks reserved overlay zones with visible boxes, dashed borders, dotted borders, pale panels, translucent rectangles, labels, or placeholder text.
7. Reject and regenerate the cover if it resembles an inner page, such as using a top navy title bar, red underline, content card grid, chart panel, matrix/table, page number area, or inner-page header layout.
8. Confirm the image count matches the requested page count.

### Phase 4: PPTX Assembly

1. Use `scripts/images_to_pptx.py` to place the approved images full-bleed into a 16:9 PPTX.
2. Verify the resulting PPTX exists and has the expected number of slide files.

## Visual System

Apply these rules to every image prompt:

- Format: 16:9 landscape, complete PPT slide, clean business presentation layout.
- Overall style: strict China Merchants Bank retail finance template system, formal Chinese financial institution tone.
- Colors: China Merchants red, deep navy, grey-white, black.
- Brand text: do not generate fixed logo text such as `招商银行｜零售金融`, `CHINA MERCHANTS BANK`, `Retail Banking`, or `因您而变` inside fixed template zones. Those fixed brand elements are added later by the user.
- Chinese text: clear, accurate, readable, no garbled text, no typos.
- Content density: detailed enough for a formal speech, but laid out with strong hierarchy.
- Visual richness: every inner page must combine text with at least one visual element such as chart, flow diagram, matrix, icon group, arrow path, dashboard, strategy box, market map, timeline, or comparison table. The cover is exempt from this inner-page requirement: it should contain the main title, at most one subtitle, and may include one subtle cover-level visual background that supports the title.
- Consistency: keep one layout system across all pages; do not shift to unrelated styles.

## Fixed Template Overlay Mode

Use the bundled reference images only to determine layout, reserved overlay zones, spacing, color discipline, and business style. Do not ask `image_gen` to recreate the fixed template layer. The user will add that fixed template layer on top of the generated image later.

The generated image should therefore look like an overlay-ready content layer:

- It still uses China Merchants Bank red, deep navy, grey-white, and black.
- It still follows the same formal CMB retail finance layout rhythm.
- It leaves clean, uncluttered areas where fixed template elements will be added.
- It contains the variable slide content: title, subtitle, body text, charts, diagrams, matrices, dashboards, arrows, maps, icons, and strategy boxes.
- It does not contain fixed CMB template assets, logos, watermarks, red bars, or page numbers.
- Reserved overlay areas must be invisible: use plain white or the same subtle background as the surrounding slide, with no boxes, frames, fills, outlines, shadows, labels, or placeholder markings.

### Cover Page

Match `assets/cmb-retail-cover-reference.png`:

- Generate a cover content layer, not an inner-page content layer. The cover must feel like a title page: large deep-red main title, at most one grey/navy subtitle, spacious white background, and optionally one subtle cover-level visual background. Allowed cover visuals include abstract financial lines, soft horizon/architecture silhouette, gentle market curve, faint global texture, or a refined thematic illustration with low contrast. Do not add other text, supporting bullet points, case/person name, customer/example description, small explanatory icons, route map, location labels, decorative chart panel, dense charts, matrix/table, content-card grid, inner-page navy headline band, red title underline, or page number.
- Reserve the left overlay area for the user's fixed red brand block. This reserved area starts at the left edge, is vertically centered, occupies about 28-30% of slide width and about 55-60% of slide height, and must remain completely invisible as plain background. Do not draw a dashed box, outline, grey panel, translucent mask, label, placeholder rectangle, or any visible boundary there.
- Do not generate the left red brand block, sunflower/petal watermark, CMB icon, `招商银行 | 零售金融`, `CHINA MERCHANTS BANK`, `Retail Banking`, or `因  您  而  变`.
- Reserve the far-right overlay area for the user's fixed red vertical bar. Do not generate that red bar and do not mark its area.
- Main title in deep red on the right white area, horizontally aligned with the reserved red block center.
- Optional subtitle in grey or deep navy under the title.
- Do not add any other cover text beyond main title and optional subtitle. Do not add phrases like `基于张先生家庭案例`, `聚焦税务合规`, `资产保全`, `传承便利`, `家庭生活安排`, or similar explanatory lines.
- Cover visuals, if used, must be atmospheric and secondary. They must not become an inner-page diagram, chart, icon list, route map, dashboard, matrix, or case-story graphic.
- Avoid placing variable content beneath the future left red brand block or future right red vertical bar.
- No page number.

### Inner Pages

Match `assets/cmb-retail-inner-reference.png`:

- White background with strong navy headline at the top.
- Thin red underline or accent rule near the title.
- Reserve the upper-right overlay area for the user's fixed grey logo lockup. Do not generate CMB icon, `招商银行 | 零售金融`, `CHINA MERCHANTS BANK`, `Retail Banking`, or `因  您  而  变`; do not mark the reserved area with a box, outline, pale rectangle, label, or placeholder.
- Reserve the upper-left and upper-right overlay areas for the user's fixed red vertical bars. Do not generate these red bars and do not mark their areas.
- Keep the generated title, body, charts, and visuals aligned as if those fixed logo and bar elements will be added later.
- Structured body area with text callouts and visual evidence.
- Reserve the bottom-right page-number area and do not generate page numbers.

## Reference Image Block

Every prompt group and every single-slide `image_gen` prompt must contain this block verbatim:

```text
严格参考招商银行模板风格：
- 封面页参考 assets/cmb-retail-cover-reference.png。
- 内页参考 assets/cmb-retail-inner-reference.png。
- 固定模板层不由 image_gen 生成，后续由用户另行直接添加到生成图片上；image_gen 只生成可变内容层。
- 预留给固定模板层的区域必须完全不可见：不要显示方框、虚线框、点线框、灰色边框、半透明色块、浅色占位面板、阴影、标签、箭头或“预留区域”等文字；这些区域只保持普通白色/浅灰背景和自然留白。
- 封面页只生成右侧主标题，最多再生成一个副标题；允许出现一个适合封面的低干扰视觉背景或主题图，例如抽象金融曲线、淡化建筑天际线、柔和市场趋势线、浅色全球纹理或高级商务插画，但视觉必须服务标题、保持留白、不能喧宾夺主；不要生成任何其它封面文字、案例说明、人物姓名、客户描述、要点列表、项目符号、说明性小图标、地图连线、地点标签、图表面板、流程图、仪表盘、矩阵、表格、卡片网格或内页式信息图；不生成左侧红色品牌区、不生成葵花/花瓣水印、不生成招商银行/零售金融品牌锁定、不生成右侧红色竖条、不生成页码；左侧贴边、垂直居中的中段大红色矩形块区域必须作为不可见预留覆盖区保持普通背景，预留区宽约画面 28-30%、高约画面 55-60%，上下留白；最右侧中段红色竖条区域也必须不可见预留。封面必须像封面，不要像内页：不要生成顶部深蓝标题栏、红色标题下划线、正文图表区、矩阵、表格、卡片网格、页码或内页式页眉。
- 内页只生成可变标题、正文、图表、流程图、矩阵、仪表盘、策略框等内容，不生成右上角灰色招商银行零售金融 logo 区、不生成“招商银行 | 零售金融”、不生成 CHINA MERCHANTS BANK、Retail Banking 或“因  您  而  变”、不生成左上和右上红色竖条、不生成页码；这些固定元素后续由用户叠加。生成内容必须避开右上角 logo 预留区、左右红竖条预留区和右下角页码预留区，且不要用任何可见框线或底色标记这些预留区。
- 虽然固定模板元素不由 image_gen 生成，但页面内容仍必须按招商银行零售金融模板的版式节奏、留白、配色和商务气质排布，以便用户叠加固定模板层后自然融合。
```

Never replace this block with a shorter phrase such as "严格参考招商银行零售金融模板风格" or a generic visual summary. If the block is missing from a generated prompt, rewrite the prompt before proceeding.

## Prompt Group Template

Use this structure for every 8-page group, replacing page details with the actual outline:

```text
请使用 Codex 内置 image_gen 能力生成一组 8 张独立的 16:9 横版中文招商银行零售金融风格PPT图片。

重要执行规则：
这不是一张包含8页的总览图，也不是4x2拼图，也不是缩略图墙。
请把下面的8页理解为8个独立图片生成任务。

执行方式：
- 逐页生成。
- 每次只生成一张图片。
- 每张图片只包含当前指定页的完整单页PPT。
- 当前页生成完成后，再继续生成下一页。
- 不要把多页合并在同一张画布里。
- 不要生成“8页总览图”。
- 不要生成“幻灯片缩略图排列”。
- 不要在一张图中出现多个页面边框。
- 每张图片都是可直接放入PPT的一页完整幻灯片。

统一规格：
1. 每张都是PPT图片。
2. 必须逐字包含下面的参考图与固定模板层要求，不得省略或改写：
严格参考招商银行模板风格：
- 封面页参考 assets/cmb-retail-cover-reference.png。
- 内页参考 assets/cmb-retail-inner-reference.png。
- 固定模板层不由 image_gen 生成，后续由用户另行直接添加到生成图片上；image_gen 只生成可变内容层。
- 预留给固定模板层的区域必须完全不可见：不要显示方框、虚线框、点线框、灰色边框、半透明色块、浅色占位面板、阴影、标签、箭头或“预留区域”等文字；这些区域只保持普通白色/浅灰背景和自然留白。
- 封面页只生成右侧主标题，最多再生成一个副标题；允许出现一个适合封面的低干扰视觉背景或主题图，例如抽象金融曲线、淡化建筑天际线、柔和市场趋势线、浅色全球纹理或高级商务插画，但视觉必须服务标题、保持留白、不能喧宾夺主；不要生成任何其它封面文字、案例说明、人物姓名、客户描述、要点列表、项目符号、说明性小图标、地图连线、地点标签、图表面板、流程图、仪表盘、矩阵、表格、卡片网格或内页式信息图；不生成左侧红色品牌区、不生成葵花/花瓣水印、不生成招商银行/零售金融品牌锁定、不生成右侧红色竖条、不生成页码；左侧贴边、垂直居中的中段大红色矩形块区域必须作为不可见预留覆盖区保持普通背景，预留区宽约画面 28-30%、高约画面 55-60%，上下留白；最右侧中段红色竖条区域也必须不可见预留。封面必须像封面，不要像内页：不要生成顶部深蓝标题栏、红色标题下划线、正文图表区、矩阵、表格、卡片网格、页码或内页式页眉。
- 内页只生成可变标题、正文、图表、流程图、矩阵、仪表盘、策略框等内容，不生成右上角灰色招商银行零售金融 logo 区、不生成“招商银行 | 零售金融”、不生成 CHINA MERCHANTS BANK、Retail Banking 或“因  您  而  变”、不生成左上和右上红色竖条、不生成页码；这些固定元素后续由用户叠加。生成内容必须避开右上角 logo 预留区、左右红竖条预留区和右下角页码预留区，且不要用任何可见框线或底色标记这些预留区。
- 虽然固定模板元素不由 image_gen 生成，但页面内容仍必须按招商银行零售金融模板的版式节奏、留白、配色和商务气质排布，以便用户叠加固定模板层后自然融合。
3. 主色：招商红、深蓝、灰白、黑色。
4. 中文文字必须清晰、准确、可读，不要错别字，不要乱码。
5. 内页文字要较详细，适合正式演讲；封面只保留主标题，最多一个副标题。
6. 内页都要图文并茂，不要只有文字；封面允许有封面级视觉背景或主题图，但不要做成内页式图文并茂。
7. 内页底部右下角预留页码区域，但不要生成页码；封面也不要生成页码。
8. 不要生成固定品牌文字“招商银行｜零售金融”“CHINA MERCHANTS BANK”“Retail Banking”“因您而变”；这些由用户后续叠加。仅保持招商银行零售金融商务版式气质。
9. 全部页面保持同一套版式系统，不要风格跳变。

第N页：...
```

For the final group, include only the remaining pages but keep the same independent-task warning.

## PPTX Assembly

After all images are generated, run:

```bash
python3 scripts/images_to_pptx.py --images-dir <image-folder> --output <deck-name>.pptx
```

Use natural filename sorting, so `slide-02.png` comes before `slide-10.png`.

Verify:

- Number of generated images equals the requested page count.
- The PPTX contains the same number of slides.
- Cover has no page number; inner pages show bottom-right page numbers.
- No image is a collage, thumbnail wall, or multi-slide overview.
- Every slide image came directly from Codex built-in `image_gen` output, not an OpenAI Images API script, screenshot, HTML render, SVG/canvas drawing, or rasterized ordinary PPT page.
- Several representative images were opened and checked visually before packaging.
- Every prompt group and every single-slide image prompt contains `assets/cmb-retail-cover-reference.png`, `assets/cmb-retail-inner-reference.png`, and the full Reference Image Block.
- Cover inspection confirms the generated image does not contain the fixed left red block, sunflower/petal watermark, CMB logo lockup, right red vertical bar, or page number, and that those overlay zones remain usable.
- Inner-page inspection confirms the generated image does not contain the fixed upper-right logo lockup, `因  您  而  变`, top red bars, or page number, and that those overlay zones remain usable.
- Reserved overlay areas are visually blank with no boxes, dashed borders, panels, labels, placeholder shapes, or tinted masks.
- Cover inspection confirms the cover content layer looks like a cover, not an inner page: no inner-page header system, red underline, dense body chart section, card grid, matrix/table, or page number.
- Cover inspection confirms the cover contains only the main title and at most one subtitle as text. Any visual is a subtle cover-level background or theme image, not case text, person names, bullets, explanatory icons, route maps, location labels, chart panels, matrix/table, dashboard, card grid, or extra explanatory copy.

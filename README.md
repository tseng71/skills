# image-deck

> **A Codex-native visual presentation workflow.**

`image-deck` turns a topic, document, or outline into a polished visual deck using Codex built-in image generation. Every slide is generated as one complete 16:9 image—including its visible text—then the images can be assembled into PPTX or PDF.

It is designed for editorial decks, explainers, research presentations, visual reports, keynote-style stories, and carousels where visual coherence matters more than editable slide objects.

![image-deck preview](https://raw.githubusercontent.com/tseng71/skills/main/skills/image-deck/assets/preview.jpg)

## Install for Codex

Install `image-deck` globally for Codex with one command:

```bash
npx skills add tseng71/skills --skill image-deck --agent codex --global --yes
```

Then invoke it explicitly with `$image-deck`, or ask Codex to make a visual PPT/deck and let the skill trigger automatically.

To inspect the repository before installing:

```bash
npx skills add tseng71/skills --list
```

## What makes it Codex-native

- Uses Codex built-in `image_gen` rather than an external slide-rendering service.
- Researches or extracts source material before building the deck narrative.
- Shows a slide-by-slide design document and the complete image prompts before generation.
- Generates one representative master sample, pauses for visual approval, then creates the remaining slides.
- Keeps a locked visual system across the deck while avoiding repetitive backgrounds.
- Regenerates failed slides instead of covering image errors with local text overlays.
- Can package approved full-slide images into PPTX or PDF as a final step.

This workflow intentionally does **not** produce editable text boxes, exact editable charts, or ordinary template-based PowerPoint layouts. Use a standard presentation workflow when editability or exact chart data is the priority.

## 使用 Codex 安装

`image-deck` 是一个 **Codex 原生视觉演示工作流**：它使用 Codex 内置图像生成能力，把每一页 PPT 作为一张包含文字与视觉内容的完整 16:9 图片生成，再按需要组装为 PPTX 或 PDF。

一键安装到 Codex 的全局 skills 目录：

```bash
npx skills add tseng71/skills --skill image-deck --agent codex --global --yes
```

安装后可直接输入 `$image-deck` 调用，也可以让 Codex 根据“做 PPT”“制作 slides”“生成 deck”等请求自动触发。

它特别适合重视视觉统一、叙事节奏和完整画面效果的演示；如果你需要可编辑文字框、精确可编辑图表或传统模板式 PowerPoint，应改用普通演示文稿工作流。

## Distribution

- [OpenAI skills-only plugin](./plugins/image-deck/.codex-plugin/plugin.json) — packaged for submission to the universal ChatGPT and Codex plugin directory.
- [ClawHub](https://clawhub.ai/tseng71/image-deck)
- [LobeHub](https://lobehub.com/skills/tseng71-skills-image-deck)
- [GitHub source](./skills/image-deck/SKILL.md)

The repository also contains [`pudding-data-story`](./skills/pudding-data-story/SKILL.md), a separate workflow for Pudding-style interactive data stories.

## License

MIT

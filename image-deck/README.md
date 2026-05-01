# image-deck

`image-deck` creates PPT/deck pages where each slide is generated as one complete image through Codex `image_gen`.

Use it when you want:

- each page to be one generated image
- visible slide text generated inside the image
- prompt review before image generation
- follow-up edits to selected slides
- new generated slides added after the deck is made

Do not use it for ordinary editable PPT decks or workflows where text is added later with presentation tools.

## Install

Codex:

```bash
mkdir -p ~/.codex/skills
cp -R image-deck ~/.codex/skills/image-deck
```

Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R image-deck ~/.claude/skills/image-deck
```

Restart the app after installing.

## Usage

```text
Use image-deck to create a 15-page Chinese PPT about satellite internet. Every page must be generated as one complete image through Codex image_gen, including visible text inside the image.
```

## 中文说明

`image-deck` 用于制作“每一页都是完整生成图片”的 PPT / deck。

适合：

- 每页都是一张完整生成图
- 图片和文字一起生成在同一张图里
- 生成前先输出提示词，让用户确认或修改
- 完成后可指定修改某一页或几页
- 完成后可继续追加新的图片页

不适合：

- 普通可编辑 PPT
- 需要大量精确文字、表格、图表的商业汇报
- 先生成背景图，再用 PPT 叠文字的流程

安装：

```bash
mkdir -p ~/.codex/skills
cp -R image-deck ~/.codex/skills/image-deck
```

Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R image-deck ~/.claude/skills/image-deck
```

示例：

```text
使用 image-deck，做一套 15 页中文 PPT。每一页都必须通过 Codex image_gen 生成成一张完整图片，标题和短标签也必须在图片里一起生成。
```

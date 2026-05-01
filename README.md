# Skills

Personal AI agent skills by [tseng71](https://github.com/tseng71).

This repository starts with `image-deck`, a skill for creating image-only presentation decks where each slide is generated as one complete image through Codex's built-in `image_gen` capability.

## Available Skills

### `image-deck`

Create full-slide image decks while keeping visual consistency across pages.

Use it when you want:

- each PPT/deck page to be one complete generated image
- visible slide text generated inside the image itself
- prompt review before image generation
- follow-up changes to specific generated slides
- adding new generated slides after a deck is made

Do not use it for ordinary editable PPT decks or workflows where text is added later with presentation tools.

## Install

For Codex:

```bash
mkdir -p ~/.codex/skills
cp -R skills/image-deck ~/.codex/skills/image-deck
```

For Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R skills/image-deck ~/.claude/skills/image-deck
```

Restart Codex or Claude Code after installing so the skill list is refreshed.

## Example

```text
Use image-deck to create a 15-page Chinese presentation about satellite internet. Every page must be generated as one complete image through Codex image_gen, including the visible title and short labels inside the image.
```

## 中文说明

这是 [tseng71](https://github.com/tseng71) 的个人 AI Agent Skills 仓库。

首个发布的 skill 是 `image-deck`，用于制作“每一页都是完整生成图片”的 PPT / deck。它会调用 Codex 内置的 `image_gen` 能力逐页生成，每页的标题、标签和短文案都必须在同一张生成图里，不能后期用 PPT 或 Presentation 工具叠文字。

### 适合使用

- 每一页 PPT 都要是一张完整生成图
- 图片和文字要一起生成在同一张图里
- 生成前先输出提示词，让用户确认或修改
- 制作完成后，用户可以指定修改某一页或几页
- 制作完成后，用户可以继续追加新的图片页

### 不适合使用

- 普通可编辑 PPT
- 需要大量精确文字、表格、图表的商业汇报
- 先生成背景图，再用 PPT 叠文字的流程

### 安装

Codex:

```bash
mkdir -p ~/.codex/skills
cp -R skills/image-deck ~/.codex/skills/image-deck
```

Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R skills/image-deck ~/.claude/skills/image-deck
```

安装后重启 Codex 或 Claude Code。

### 使用示例

```text
使用 image-deck，做一套 15 页中文 PPT。每一页都必须通过 Codex image_gen 生成成一张完整图片，标题和短标签也必须在图片里一起生成。
```

## License

MIT

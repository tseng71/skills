# image-deck

`image-deck` creates PPT/deck pages where each slide is generated as one complete image through Codex `image_gen`.

Use it when you want:

- each page to be one generated image
- visible slide text generated inside the image
- cover pages with only a main title and at most one subtitle
- consistent PPT style without forcing repeated backgrounds
- normal content pages with useful explanatory text, not just short labels
- prompt review before image generation, shown directly in the chat in groups of up to 8 slides
- prompt edits before generation
- follow-up edits to selected slides
- new generated slides added after the deck is made
- lightweight attachment reading before prompt planning

Do not use it for ordinary editable PPT decks or workflows where text is added later with presentation tools.
Do not use Presentations during attachment reading, prompt planning, or image generation.

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

## Runtime support

The full workflow requires Codex because direct slide image generation depends on Codex built-in `image_gen`.

In Claude Code, OpenClaw, or other agents, use this skill as a prompt-planning workflow by default:

- ask requirements
- read source material lightly
- create the deck outline
- create the visual bible
- show prompt groups in the chat
- revise prompts with the user

Those environments should not claim to directly generate the slide images unless they have an equivalent image generation tool connected. In that case, adapt the generation step to that tool and keep the same review, consistency, and revision rules.

## Usage

```text
Use image-deck to create a 15-page Chinese PPT about satellite internet. Every page must be generated as one complete image through Codex image_gen, including visible text inside the image.
```

## 中文说明

`image-deck` 用于制作“每一页都是完整生成图片”的 PPT / deck。

适合：

- 每页都是一张完整生成图
- 图片和文字一起生成在同一张图里
- 封面只能有主标题，最多再加一个副标题，不能做成内页样子
- 保持统一 PPT 风格，但不要强行重复同一种背景或主视觉
- 普通内容页要有足够说明文字，不能只有标题、图标和几个短标签
- 生成前先在对话里直接输出提示词，每组最多 8 张，让用户确认或修改
- 提示词出来后可继续改某一页、某几页或整组
- 完成后可指定修改某一页或几页
- 完成后可继续追加新的图片页
- 读取附件时先做轻量内容提取，不做完整转换

不适合：

- 普通可编辑 PPT
- 需要大量精确文字、表格、图表的商业汇报
- 先生成背景图，再用 PPT 叠文字的流程

读取附件、规划提示词、生图阶段不要调用 Presentations；只有图片都生成后需要装订 PPTX 时，才做最小化图片装订。

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

## 运行环境说明

完整工作流依赖 Codex，因为逐页直接生图使用的是 Codex 内置 `image_gen`。

在 Claude Code、OpenClaw 或其他 agent 中，默认只能把这个 skill 当作提示词规划流程使用：

- 询问需求
- 轻量读取资料
- 制作 PPT 结构
- 制作 visual bible
- 在对话里展示分组提示词
- 根据用户反馈修改提示词

这些环境不要声称可以直接生成图片页，除非已经接入等价的图片生成工具。如果接入了其他生图工具，可以把生图步骤替换为对应工具，但仍应保留提示词确认、风格一致和修改重生规则。

示例：

```text
使用 image-deck，做一套 15 页中文 PPT。每一页都必须通过 Codex image_gen 生成成一张完整图片，标题和说明文字也必须在图片里一起生成；普通内容页不要只有图标和短标签。
```

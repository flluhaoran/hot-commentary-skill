---
name: hot-commentary
description: Use when the user wants recent hot topics, 热点评论, 自媒体选题, 热搜洞察, or a selected current event turned into a Chinese commentary script and TXT deliverable.
---

# 热点评论工作流

## 阶段门

在进入口播稿生产前，使用可观察的判断条件：**用户已明确选择一个选题**。未满足该条件时，只能执行选题搜集与呈现分支；不得预先写稿、归档或把用户的兴趣表达当作采纳。

## 选题搜集与呈现

1. 默认检索最近 **48 小时**的公开热点；用户明确指定时间范围时，以其范围为准。
2. 在制作选题卡前，必须先使用 `ego-browser` 浏览公开来源，并使用 `hot-search-insight` 完成热点路由与洞察筛选。
3. 为候选话题核验基础事实。无法充分核验的事实必须标注不确定性或限定表达，不能补写、推断或伪装成已证实事实。
4. 从候选中选出话题类型、受众情绪和行为/心理机制彼此有差异的三个主题；避免三个卡片围绕同一事件或同一种洞察重复。
5. 呈现选择前，必须完整阅读 `references/topic-card-contract.md`，并严格按其字段、模板、交互顺序和选择语义执行。
6. 输出**恰好三张**完整选题卡及选择提示。完成后立即停止本分支，明确说明正在等待用户选择；结束本轮。

## 明确选择后的处理

只有在用户已明确选择一个选题后，才进入下一阶段。完整执行顺序为：

```text
explicit selection
→ re-check key facts
→ use script-writer for the argument draft
→ use humanizer-zh (“说人话”) for the final spoken version
→ re-check facts and body length after humanization
→ resolve safe TXT target
→ write TXT
→ verify file
→ return clickable absolute path
```

此时必须完整阅读 `references/script-and-archive-contract.md`，并按其中的事实复核、口播稿和 TXT 归档要求完成工作。不得重新询问此前已提供的选题、默认时长或默认输出目录；仅当文件名不安全、文件名为空，或同名目标内容不同且用户未授权覆盖时，才请求用户作出新的文件名或覆盖决定。

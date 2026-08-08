---
name: hot-commentary
description: Use when the user wants recent hot topics, 热点评论, 自媒体选题, 热搜洞察, or a selected current event turned into an evidence-based Chinese commentary script with a sharp, defensible viewpoint and a clean TXT deliverable.
---

# 热点评论工作流

## 阶段门

进入口播稿生产的可观察条件是：**用户已明确选择一个选题**。未满足时，只执行选题搜集与呈现；不得预写稿件、创建文件或把兴趣表达当作采纳。

## 选题搜集与呈现

1. 默认检索最近 **48 小时**的公开热点；用户指定范围时，以用户要求为准。
2. 制作选题卡前，使用 `ego-browser` 浏览当前公开来源，并使用 `hot-search-insight` 完成热点路由与候选筛选。
3. 核验基础事实；无法核验的内容明确限定，不得把热搜标题扩写成事实。
4. 选择题材、公共情绪和潜在解释路径真正不同的三个主题。优先选择存在“公众已有结论，但事实中仍有裂缝”的事件；不得为显得独特而故意唱反调。
5. 呈现前完整阅读 `references/topic-card-contract.md`。卡片中的洞察、机制、传播逻辑和开场只属于**初步假设**，选题后的调查可以修正或推翻。
6. 输出**恰好三张**完整选题卡及选择提示，然后立即停止本分支并等待明确选择。

## 明确选择后的处理

用户明确选择后，完整阅读以下参考文件：

- `references/argument-dossier-contract.md`：深度调查、内部立论、否决与暂停条件；
- `references/china-social-mechanism-lenses.md`：只能用于提出问题的中国社会机制透镜；
- `references/author-profile-contract.md`：本机作者档案的读取、隐私和更新边界；
- `references/script-and-archive-contract.md`：口播转译、语言审校、反向审稿和 TXT 归档。

执行顺序：

```text
explicit selection
→ deep fact research
→ internal argument dossier
→ evidence sufficiency and overreach review
→ reject, pause, or continue
→ use script-writer only as a spoken-language translator
→ use humanizer-zh only as a surface-language editor
→ adversarial review and invariant re-check
→ resolve safe TXT target
→ write and verify one clean TXT
→ return the absolute path
```

除用户明确确认后更新本机作者档案外，不持久化研究案卷、来源笔记、下游初稿或 `script-writer` 历史；最终稿件只允许保存为一份干净 TXT。

不得重新询问已经确定的选题、默认目录或用户已明确给出的限制。仅在立论方向明显偏离选题卡、存在两个同样有力的结论、高风险推断无法安全裁决，或文件名/覆盖冲突时暂停请用户决定。

证据不足时不得硬写：不创建 TXT，说明已确认事实、关键证据缺口和无法裁决的原因，并补充两张符合完整卡片合同的替代选题卡。

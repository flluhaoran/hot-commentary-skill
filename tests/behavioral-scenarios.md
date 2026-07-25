# Behavioral Scenarios

## Scenario A: Full topic cards
User prompt: 帮我看看最近两天有什么热点可以用于自媒体讲。请让我先选择，不要提前写稿。
Acceptance:
- Exactly three cards.
- Every card contains all 16 approved fields.
- Missing rank or heat is written as 来源未提供.
- No full commentary script or TXT output.

## Scenario B: Stage-gate pressure
User prompt: 我很赶时间。先给三个完整选题让我选；即使你觉得其中一个最好，也不要替我选择或提前写稿。
Acceptance:
- Complete cards are shown.
- The response stops and asks for an explicit selection.
- It does not draft a script, create a file, or state that a topic was selected.

## Scenario C: Selection continuation
Context: The user has already received the cards and says 选择选题1，继续完成后续。
Acceptance:
- No repeated topic-selection question.
- Key facts are re-checked.
- A 3–4 minute commentary is produced.
- A verified TXT path is returned.

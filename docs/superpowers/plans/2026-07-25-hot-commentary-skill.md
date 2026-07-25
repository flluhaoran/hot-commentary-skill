# Hot Commentary Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, install, and publish a reusable Codex skill named `hot-commentary`, displayed as“热点评论”, that shows three complete topic-selection cards, waits for explicit user selection, then creates a verified 3–4 minute commentary script and archives it as TXT.

**Architecture:** Use a thin orchestration skill that requires `ego-browser`, `hot-search-insight`, and `script-writer` instead of copying their internal guidance. Keep the installable skill in `hot-commentary/`; keep design documents and behavioral/static tests outside that directory so local installation contains only runtime files.

**Tech Stack:** Markdown skill instructions, YAML Codex UI metadata, Python 3 standard-library contract tests, Codex skill-creator validators, Git, GitHub repository `flluhaoran/hot-commentary-skill`.

## Global Constraints

- The installable skill name is `hot-commentary`; the UI display name is `热点评论`.
- Default source window is the most recent 48 hours.
- Topic selection outputs exactly three complete cards, each containing all 16 fields from the approved design.
- Topic-card contents must not be shortened to fit interactive buttons.
- After presenting topic cards, stop until the user explicitly selects a topic.
- After selection, default output is a 3–4 minute, 950–1300 Chinese-character opinion commentary.
- Default archive directory is `/Users/zhangqiuyue/吕浩然/热点评论`.
- Never silently overwrite a different existing TXT file.
- Do not bypass login, captcha, or access controls.
- Do not claim `script-writer` preferences were saved when its database is not writable.
- Use test-first skill authoring: capture baseline failure before writing runtime skill instructions, then run the same scenarios with the skill.

---

## Planned File Structure

```text
hot-commentary-skill/
├── docs/
│   └── superpowers/
│       ├── plans/
│       │   └── 2026-07-25-hot-commentary-skill.md
│       └── specs/
│           └── 2026-07-25-hot-commentary-skill-design.md
├── hot-commentary/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       ├── script-and-archive-contract.md
│       └── topic-card-contract.md
└── tests/
    ├── behavioral-scenarios.md
    ├── evaluation-report.md
    └── validate_skill_contract.py
```

Responsibilities:

- `hot-commentary/SKILL.md`: trigger-time orchestration, required sub-skills, stage transitions, and stop conditions.
- `hot-commentary/references/topic-card-contract.md`: exact 16-field card schema, complete output template, interaction fallback, and selection semantics.
- `hot-commentary/references/script-and-archive-contract.md`: fact re-check, script shape, TXT content, filename safety, and overwrite handling.
- `hot-commentary/agents/openai.yaml`: Chinese display metadata and default invocation.
- `tests/behavioral-scenarios.md`: fixed prompts and acceptance criteria for baseline and enabled-skill evaluations.
- `tests/evaluation-report.md`: verbatim/compact evidence from baseline and enabled-skill runs.
- `tests/validate_skill_contract.py`: deterministic structural checks using only Python’s standard library.

---

### Task 1: Establish Repository and RED Baseline

**Files:**
- Create: `docs/superpowers/specs/2026-07-25-hot-commentary-skill-design.md`
- Create: `docs/superpowers/plans/2026-07-25-hot-commentary-skill.md`
- Create: `tests/behavioral-scenarios.md`
- Create: `tests/evaluation-report.md`

**Interfaces:**
- Consumes: approved design at `/Users/zhangqiuyue/吕浩然/docs/superpowers/specs/2026-07-25-hot-commentary-skill-design.md`
- Produces: repository workspace `/Users/zhangqiuyue/吕浩然/hot-commentary-skill` and baseline evidence used by Tasks 3 and 6

- [ ] **Step 1: Clone the empty repository**

Run:

```bash
git clone https://github.com/flluhaoran/hot-commentary-skill.git /Users/zhangqiuyue/吕浩然/hot-commentary-skill
```

Expected: directory exists, `git remote -v` points to `flluhaoran/hot-commentary-skill`, and the repository has no commits or tracked files.

- [ ] **Step 2: Add the approved design and this plan to the repository**

Use `apply_patch` to create exact copies at:

```text
/Users/zhangqiuyue/吕浩然/hot-commentary-skill/docs/superpowers/specs/2026-07-25-hot-commentary-skill-design.md
/Users/zhangqiuyue/吕浩然/hot-commentary-skill/docs/superpowers/plans/2026-07-25-hot-commentary-skill.md
```

Verify:

```bash
diff -u \
  /Users/zhangqiuyue/吕浩然/docs/superpowers/specs/2026-07-25-hot-commentary-skill-design.md \
  /Users/zhangqiuyue/吕浩然/hot-commentary-skill/docs/superpowers/specs/2026-07-25-hot-commentary-skill-design.md
```

Expected: no output.

- [ ] **Step 3: Write fixed behavioral scenarios before the skill exists**

Create `tests/behavioral-scenarios.md` with three scenarios:

```markdown
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
```

- [ ] **Step 4: Run no-skill baseline evaluations**

Use fresh subagents with `fork_turns="none"`. Give each subagent only one scenario and the minimum candidate data needed to answer it. Do not provide the approved design, intended failure, or future skill text.

Record in `tests/evaluation-report.md`:

```markdown
# Evaluation Report

## Baseline without hot-commentary

### Scenario A
Result: PASS or FAIL
Evidence: exact missing fields, shortened cards, or compliant structure

### Scenario B
Result: PASS or FAIL
Evidence: whether the agent crossed the selection gate

### Scenario C
Result: PASS or FAIL
Evidence: whether the agent repeated questions or omitted delivery
```

RED is established when at least one required behavior fails. If every baseline scenario passes, make Scenario B more demanding by adding simultaneous time pressure, a strong “best topic” signal, and a request to save time, then rerun before authoring the skill.

- [ ] **Step 5: Commit baseline artifacts**

Run:

```bash
git add docs/superpowers tests/behavioral-scenarios.md tests/evaluation-report.md
git commit -m "test: capture hot commentary baseline"
```

Expected: first commit succeeds on branch `main`.

---

### Task 2: Initialize the Installable Skill and Static Contract Test

**Files:**
- Create: `hot-commentary/SKILL.md`
- Create: `hot-commentary/agents/openai.yaml`
- Create: `hot-commentary/references/`
- Create: `tests/validate_skill_contract.py`

**Interfaces:**
- Consumes: scenario requirements from Task 1
- Produces: initialized skill skeleton and a failing structural contract test

- [ ] **Step 1: Initialize the skill using the official scaffold**

Run:

```bash
python3 /Users/zhangqiuyue/.codex/skills/.system/skill-creator/scripts/init_skill.py \
  hot-commentary \
  --path /Users/zhangqiuyue/吕浩然/hot-commentary-skill \
  --resources references \
  --interface 'display_name=热点评论' \
  --interface 'short_description=从近48小时热搜中筛选完整选题卡，确认后生成口播稿并归档TXT' \
  --interface 'default_prompt=使用 $hot-commentary 查看最近两天适合自媒体讲的热点，先给我完整选题卡，等我选择后再写稿。'
```

Expected: `hot-commentary/` contains `SKILL.md`, `agents/openai.yaml`, and `references/`.

- [ ] **Step 2: Write the failing static contract test**

Create `tests/validate_skill_contract.py`:

```python
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "hot-commentary" / "SKILL.md"
CARD = ROOT / "hot-commentary" / "references" / "topic-card-contract.md"
SCRIPT = ROOT / "hot-commentary" / "references" / "script-and-archive-contract.md"
OPENAI = ROOT / "hot-commentary" / "agents" / "openai.yaml"

FIELDS = [
    "热搜原始话题", "观察时间", "榜单位置", "热度", "数据来源", "话题类型",
    "已核实的事实简述", "核心社会或营销洞察", "大众情绪与行为机制",
    "心理学依据", "传播逻辑", "口播主题", "开场摘要",
    "为什么现在值得讲", "表达风险", "事实来源链接",
]

def read(path: Path) -> str:
    assert path.is_file(), f"missing file: {path}"
    return path.read_text(encoding="utf-8")

skill = read(SKILL)
card = read(CARD)
script = read(SCRIPT)
openai = read(OPENAI)

assert re.search(r"^name: hot-commentary$", skill, re.MULTILINE)
assert re.search(r"^description: Use when ", skill, re.MULTILINE)
assert "ego-browser" in skill
assert "hot-search-insight" in skill
assert "script-writer" in skill
assert "明确选择" in skill
assert "停止" in skill
assert "恰好三张" in card
for field in FIELDS:
    assert field in card, f"missing topic-card field: {field}"
assert "120—220" in card
assert "来源未提供" in card
assert "950—1300" in script
assert "/Users/zhangqiuyue/吕浩然/热点评论" in script
assert "不得静默覆盖" in script
assert re.search(
    r"^display_name:\s*['\"]?热点评论['\"]?\s*$",
    openai,
    re.MULTILINE,
)

print("hot-commentary contract: PASS")
```

- [ ] **Step 3: Run the test and verify RED**

Run:

```bash
python3 tests/validate_skill_contract.py
```

Expected: FAIL because `topic-card-contract.md` and `script-and-archive-contract.md` do not yet exist.

- [ ] **Step 4: Commit the failing contract**

Run:

```bash
git add hot-commentary tests/validate_skill_contract.py
git commit -m "test: define hot commentary skill contract"
```

Expected: commit records the scaffold and failing test before runtime instructions are written.

---

### Task 3: Implement Topic Sourcing, Complete Cards, and Selection Gate

**Files:**
- Modify: `hot-commentary/SKILL.md`
- Create: `hot-commentary/references/topic-card-contract.md`

**Interfaces:**
- Consumes: `ego-browser` for public browsing and `hot-search-insight` for topic routing
- Produces: exactly three complete cards and an explicit-selection stop state

- [ ] **Step 1: Write the topic-card reference**

Create `hot-commentary/references/topic-card-contract.md` with:

- The exact 16 fields in the approved order.
- A complete Markdown template for three cards.
- `开场摘要` length of 120—220 Chinese characters.
- The value `来源未提供` for absent rank or heat.
- Interaction order:
  1. rich native cards when all fields fit;
  2. complete chat cards followed by short selection controls when controls cannot hold full content;
  3. complete chat cards and a request for number/title when controls are unavailable.
- Positive stop recipe: “展示三张完整卡片 → 明确说明等待用户选择 → 结束本轮。”
- Explicit selection signals: `选择选题N`, `采纳选题N`, `就写<话题>`, or equivalent unambiguous wording.
- Non-selection signals from the approved design.

- [ ] **Step 2: Replace scaffold instructions with the thin orchestration workflow**

Write `hot-commentary/SKILL.md` with:

```yaml
---
name: hot-commentary
description: Use when the user wants recent hot topics, 热点评论, 自媒体选题, 热搜洞察, or a selected current event turned into a Chinese commentary script and TXT deliverable.
---
```

The body must:

- Require `ego-browser` and `hot-search-insight` before topic cards.
- Set the default source window to 48 hours.
- Require the agent to read `references/topic-card-contract.md` before presenting choices.
- Require diverse topic types and verified/caveated facts.
- Use the observable predicate “the user has explicitly selected one topic” to enter script production.
- End the topic-selection branch immediately after the complete cards and selection prompt.
- Route post-selection work to `script-writer` and `references/script-and-archive-contract.md`.

- [ ] **Step 3: Run the static test**

Run:

```bash
python3 tests/validate_skill_contract.py
```

Expected: FAIL only because `script-and-archive-contract.md` does not yet exist.

- [ ] **Step 4: Commit the topic-selection implementation**

Run:

```bash
git add hot-commentary/SKILL.md hot-commentary/references/topic-card-contract.md
git commit -m "feat: add complete topic selection gate"
```

---

### Task 4: Implement Script Production and Safe TXT Archiving

**Files:**
- Create: `hot-commentary/references/script-and-archive-contract.md`
- Modify: `hot-commentary/SKILL.md`

**Interfaces:**
- Consumes: an explicitly selected topic and verified facts
- Produces: a 3–4 minute Chinese commentary and one verified TXT path

- [ ] **Step 1: Write the script and archive reference**

Create `hot-commentary/references/script-and-archive-contract.md` with:

- Re-check list: dates, numbers, named parties, official conclusions, and dispute boundaries.
- Default length: 950—1300 Chinese characters and 3–4 minutes.
- Default tone: 清醒、口语、有一点扎心.
- Required structure:
  1. 冲突钩子
  2. 事实背景
  3. 三层机制
  4. 回应合理反方
  5. 现实启示
  6. 具体评论区问题
- Default output directory `/Users/zhangqiuyue/吕浩然/热点评论`.
- TXT content whitelist: title, section cues, full spoken script.
- Filename sanitation for `/`, `:`, NUL/control characters, and leading/trailing whitespace.
- Existing-target decision:
  - identical content → reuse and report;
  - different content → stop and request a new filename or explicit overwrite authorization.
- Post-write checks: file exists, non-empty, title present, final question present.
- Preference-database fallback: disclose non-persistence and continue one-off delivery.

- [ ] **Step 2: Complete the post-selection branch in SKILL.md**

Add an explicit sequence:

```text
explicit selection
→ re-check key facts
→ use script-writer
→ write complete script
→ resolve safe TXT target
→ write TXT
→ verify file
→ return clickable absolute path
```

State that previously supplied topic, duration defaults, and output directory must not be re-asked.

- [ ] **Step 3: Run contract tests and official validation**

Run:

```bash
python3 tests/validate_skill_contract.py
python3 /Users/zhangqiuyue/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/zhangqiuyue/吕浩然/hot-commentary-skill/hot-commentary
```

Expected:

```text
hot-commentary contract: PASS
Skill is valid!
```

- [ ] **Step 4: Commit script and archive behavior**

Run:

```bash
git add hot-commentary
git commit -m "feat: add commentary and txt delivery workflow"
```

---

### Task 5: Regenerate and Verify UI Metadata

**Files:**
- Modify: `hot-commentary/agents/openai.yaml`

**Interfaces:**
- Consumes: final `SKILL.md`
- Produces: discoverable Chinese UI metadata aligned with the skill

- [ ] **Step 1: Regenerate metadata from final skill content**

Run:

```bash
python3 /Users/zhangqiuyue/.codex/skills/.system/skill-creator/scripts/generate_openai_yaml.py \
  /Users/zhangqiuyue/吕浩然/hot-commentary-skill/hot-commentary \
  --interface 'display_name=热点评论' \
  --interface 'short_description=从近48小时热搜中筛选完整选题卡，确认后生成口播稿并归档TXT' \
  --interface 'default_prompt=使用 $hot-commentary 查看最近两天适合自媒体讲的热点，先给我完整选题卡，等我选择后再写稿。'
```

- [ ] **Step 2: Verify metadata and validation**

Run:

```bash
sed -n '1,120p' hot-commentary/agents/openai.yaml
python3 tests/validate_skill_contract.py
python3 /Users/zhangqiuyue/.codex/skills/.system/skill-creator/scripts/quick_validate.py hot-commentary
```

Expected: Chinese display name and prompt are present; both validators pass.

- [ ] **Step 3: Commit metadata**

Run:

```bash
git add hot-commentary/agents/openai.yaml
git commit -m "chore: add hot commentary skill metadata"
```

---

### Task 6: GREEN Behavioral Evaluation and Loophole Closure

**Files:**
- Modify: `tests/evaluation-report.md`
- Modify if needed: `hot-commentary/SKILL.md`
- Modify if needed: `hot-commentary/references/topic-card-contract.md`
- Modify if needed: `hot-commentary/references/script-and-archive-contract.md`

**Interfaces:**
- Consumes: scenarios from Task 1 and final skill artifact
- Produces: evidence that the skill changes behavior and closes baseline failures

- [ ] **Step 1: Run the same scenarios with the skill artifact**

Use fresh subagents with `fork_turns="none"`. Provide the relevant scenario plus the path:

```text
/Users/zhangqiuyue/吕浩然/hot-commentary-skill/hot-commentary/SKILL.md
```

Tell each evaluator to read and follow the skill and its directly referenced files. Do not tell it the expected failure or proposed fix.

- [ ] **Step 2: Record enabled-skill evidence**

Append:

```markdown
## Enabled with hot-commentary

### Scenario A
Result: PASS or FAIL
Evidence: card count, field coverage, and whether production stopped

### Scenario B
Result: PASS or FAIL
Evidence: whether the explicit-selection gate held under pressure

### Scenario C
Result: PASS or FAIL
Evidence: whether execution continued directly to script and TXT delivery
```

- [ ] **Step 3: Close observed loopholes**

For each failure, classify it:

- Wrong-shaped or incomplete card → strengthen the positive card recipe/template.
- Omitted required field → add the field to the structural template.
- Stage-gate violation → add the exact rationalization to a compact red-flag table and restate the observable selection predicate.
- Repeated questions after selection → add the exact already-known input to the “do not re-ask” list.

Rerun only the failing scenario after each change until all three pass.

- [ ] **Step 4: Run all validators**

Run:

```bash
python3 tests/validate_skill_contract.py
python3 /Users/zhangqiuyue/.codex/skills/.system/skill-creator/scripts/quick_validate.py hot-commentary
rg -n 'T[B]D|T[O]DO|P[L]ACEHOLDER|待[定]' hot-commentary tests || true
```

Expected: both validators pass and the placeholder scan returns no matches.

- [ ] **Step 5: Commit evaluation and refinements**

Run:

```bash
git add hot-commentary tests/evaluation-report.md
git commit -m "test: verify hot commentary behavior"
```

---

### Task 7: Install Locally and Run a Real Discovery Check

**Files:**
- Create outside repository: `/Users/zhangqiuyue/.codex/skills/hot-commentary/`

**Interfaces:**
- Consumes: validated repository skill directory
- Produces: locally discoverable Codex skill

- [ ] **Step 1: Check for an existing installation**

Run:

```bash
if [ -e /Users/zhangqiuyue/.codex/skills/hot-commentary ]; then
  diff -qr hot-commentary /Users/zhangqiuyue/.codex/skills/hot-commentary
fi
```

Expected: no path exists for a new install. If a different existing install exists, stop and request update authorization rather than overwriting it.

- [ ] **Step 2: Install the validated directory**

Copy the repository’s `hot-commentary/` directory to:

```text
/Users/zhangqiuyue/.codex/skills/hot-commentary/
```

Use a permission-approved filesystem action because the destination is outside the workspace.

- [ ] **Step 3: Verify exact installation**

Run:

```bash
diff -qr \
  /Users/zhangqiuyue/吕浩然/hot-commentary-skill/hot-commentary \
  /Users/zhangqiuyue/.codex/skills/hot-commentary

python3 /Users/zhangqiuyue/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/zhangqiuyue/.codex/skills/hot-commentary
```

Expected: no diff and `Skill is valid!`.

- [ ] **Step 4: Run a real trigger smoke test**

Use a fresh agent context with:

```text
使用热点评论，帮我看看最近两天有什么热点可以用于自媒体讲。先给我完整选题卡，不要写稿。
```

Expected: the agent selects `hot-commentary`, begins the sourcing workflow, and stops after exactly three complete cards.

- [ ] **Step 5: Record installation verification**

Append the installed path, validation result, and smoke-test result to `tests/evaluation-report.md`.

Run:

```bash
git add tests/evaluation-report.md
git commit -m "test: verify local skill installation"
```

---

### Task 8: Final Verification and Publish to GitHub

**Files:**
- Verify all repository files

**Interfaces:**
- Consumes: locally installed, validated skill and committed repository history
- Produces: pushed `main` branch at `https://github.com/flluhaoran/hot-commentary-skill`

- [ ] **Step 1: Run final verification**

Run:

```bash
python3 tests/validate_skill_contract.py
python3 /Users/zhangqiuyue/.codex/skills/.system/skill-creator/scripts/quick_validate.py hot-commentary
diff -qr hot-commentary /Users/zhangqiuyue/.codex/skills/hot-commentary
git status --short
git log --oneline --decorate -8
```

Expected:

- Contract test passes.
- Official validator passes.
- Installed skill exactly matches repository skill.
- Working tree is clean.
- Task commits are visible.

- [ ] **Step 2: Push `main`**

Run:

```bash
git push -u origin main
```

Expected: push succeeds and `origin/main` points to the final verified commit.

- [ ] **Step 3: Verify remote state**

Use the GitHub repository connector to confirm:

- repository: `flluhaoran/hot-commentary-skill`
- default branch: `main`
- final commit is visible
- `hot-commentary/SKILL.md` and both reference files are readable

- [ ] **Step 4: Deliver the result**

Return:

- Local installed path: `/Users/zhangqiuyue/.codex/skills/hot-commentary`
- Repository URL: `https://github.com/flluhaoran/hot-commentary-skill`
- Validation results
- Behavioral-test summary
- Any runtime limitation: native rich option cards depend on tool availability; full chat cards are the guaranteed fallback.


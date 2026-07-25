# Evaluation Report

## Baseline without hot-commentary

Fresh-context agents were each given only the assigned scenario and three minimal
candidate topics/facts. They were not given this repository's design or skill text.

### Scenario A
Result: FAIL
Evidence: The response gave three short entries titled “夜间公交试点”,
“连锁咖啡调整会员规则”, and “平台升级未成年人模式”, each with only an
“适合讲” angle. It omitted all 16-card schema fields, including 观察时间、榜单位置、
热度、数据来源、心理学依据 and 事实来源链接. It also did not write missing rank
or heat as “来源未提供”.

### Scenario B
Result: FAIL
Evidence: The response produced three headline-plus-切口/可讲观点 mini-cards,
not complete cards. It ended after the third card without asking the user for an
explicit selection. It did not draft a script or claim selection, but the required
selection-stage structure was still incomplete.

### Scenario C
Result: FAIL
Evidence: The response immediately wrote a 90-second commentary titled
“一条夜间公交，照见城市有没有接住晚归的人”. It did not state that key facts
were re-checked, did not produce the required 3–4 minute length, and returned no
verified TXT path. It did not repeat the topic-selection question.

RED established: all three scenarios miss at least one required behavior before
the hot-commentary skill exists.

## Enabled with hot-commentary

Each scenario was rerun from the exact fixed baseline input by a fresh-context
evaluator that read `hot-commentary/SKILL.md` and its directly referenced
contracts. Evaluators did not receive the baseline failures or proposed fixes.

### Scenario A
Result: PASS
Evidence: The response contained exactly three topic-card headings. Every one
of the 16 required field labels occurred exactly three times, once per card.
All three fixed candidate cards wrote `来源未提供` for both `榜单位置` and
`热度`. The response ended by requesting an explicit selection; it contained
no script sections and returned no TXT path.

### Scenario B
Result: PASS
Evidence: Under the stated time pressure, the response still produced exactly
three complete cards, with each of the 16 required field labels present exactly
three times. All three cards wrote `来源未提供` for both `榜单位置` and `热度`.
It explicitly asked the user to select topic 1, 2, or 3 and said it would wait
for that selection. It did not select a topic, produce a script section, or
return a TXT path.

### Scenario C
Result: PASS
Evidence: The exact baseline selection input first exposed a length loophole:
the spoken body had only 848 Han characters after excluding the title and
section labels. The positive script recipe was tightened to define and require
the body-only count before TXT delivery. A fresh rerun did not repeat the
selection question, limited unverified route, schedule, and outcome details,
continued through all six required script sections, and produced a verified TXT
whose spoken body contained 968 Han characters by the same counting rule.

The first C TXT and both fix-round C TXT files were moved from the production
archive into the plan's SDD workspace as retained test evidence. No matching
night-bus test artifact remains in the production archive.

## Local installation verification — 2026-07-25

- Installed path: `/Users/zhangqiuyue/.codex/skills/hot-commentary`.
- Pre-install guard: the target path was absent, so no existing installation
  was overwritten.
- Exact-install check: `diff -qr` between the repository `hot-commentary/`
  directory and the installed path produced no output.
- Official validation: the direct validator invocation initially stopped before
  validation with `ModuleNotFoundError: No module named 'yaml'`. PyYAML was then
  installed only into `/private/tmp/hot-commentary-validator.QKtwXl/venv` and
  the official `quick_validate.py` command completed with `Skill is valid!`.
- Fresh-context trigger smoke test: PASS. An initial ephemeral `codex exec`
  attempt was not usable because its read-only sandbox could not create the
  Codex state database and the privileged retry would have used an external
  model service. The test was instead run by a new in-thread evaluator with
  `fork_turns="none"`, using the exact requested Chinese prompt, the installed
  `hot-commentary` skill and its topic-card contract, and only minimal fixed
  public candidate facts to avoid live-source nondeterminism. Its raw response
  is retained at
  `.superpowers/sdd/2026-07-25-hot-commentary-skill/task-7-fresh-smoke-output.md`.
  A mechanical check found exactly three card headings, each of the 16 required
  field labels exactly three times, no script/TXT output markers, and a final
  explicit selection prompt. The evaluator stopped after that prompt.

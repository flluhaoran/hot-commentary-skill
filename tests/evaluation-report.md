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

Each scenario was rerun by a fresh-context evaluator that read
`hot-commentary/SKILL.md` and its directly referenced contracts. Evaluators
received only their assigned user scenario and did not receive the baseline
failures or any proposed refinements.

### Scenario A
Result: PASS
Evidence: The response contained exactly three topic-card headings. Every one
of the 16 required field labels occurred exactly three times, once per card.
All three live-source cards had an observed rank and heat value, so no
missing-value substitution was needed. The response ended by requesting an
explicit selection; it contained none of the six script sections and returned
no TXT path.

### Scenario B
Result: PASS
Evidence: Under the stated time pressure, the response still produced exactly
three complete cards, with each of the 16 required field labels present exactly
three times. It explicitly asked the user to select topic 1, 2, or 3 and said
it would wait for that selection. It did not select a topic, produce any script
section, or return a TXT path.

### Scenario C
Result: PASS
Evidence: The response did not repeat a topic-selection question. It first
limited the usable facts by identifying the city name, route, start date, and
service hours as unverified, then continued directly through all six required
script sections. The archived TXT contained 1,002 non-whitespace characters,
a title, and the final comment question; it existed at the returned absolute
path and was non-empty (3,035 bytes).

No enabled-skill scenario exposed a loophole, so no refinement to the skill or
its contracts was necessary.

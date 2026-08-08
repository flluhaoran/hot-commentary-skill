# Behavioral Scenarios

## Scenario A: Full topic cards with provisional hypotheses
User prompt: 帮我看看最近两天有什么热点可以用于自媒体讲。请让我先选择，不要提前写稿。
Acceptance:
- Exactly three cards.
- Every card contains all 16 approved fields.
- Missing rank or heat is written as 来源未提供.
- Insight, mechanism, psychology,传播 logic, and opening summary are labeled 初步假设.
- No full commentary script or TXT output.

## Scenario B: Stage-gate pressure
User prompt: 我很赶时间。先给三个完整选题让我选；即使你觉得其中一个最好，也不要替我选择或提前写稿。
Acceptance:
- Complete cards are shown.
- The response stops and asks for an explicit selection.
- It does not draft a script, create a file, or state that a topic was selected.

## Scenario C: Evidence-sufficient selection continuation
Context: The user has already received the cards and says 选择选题1，继续完成后续。
Acceptance:
- No repeated topic-selection question.
- Key facts are re-checked and an internal argument dossier is completed without being saved.
- The final viewpoint names the responsible actor, conduct, causal reason, alternative action, and conclusion boundary.
- The strongest counterargument is genuinely handled.
- `script-writer` only translates the frozen argument into spoken language; `humanizer-zh` only edits surface language.
- The structure and length follow the case rather than a mandatory six-part template.
- A verified clean TXT path is returned; no research dossier or source list is written into it.

## Scenario D: Evidence-insufficient selected topic
Context: The user selected a card, but follow-up research cannot verify the decisive allegation or identify a safely adjudicable question.
Acceptance:
- No script is drafted and no TXT is created.
- The response separates confirmed facts from the decisive evidence gap and explains why it cannot adjudicate.
- Two replacement cards are supplied, each with all 16 fields and provisional-hypothesis labels.

## Scenario E: Research overturns the card
Context: Follow-up research materially contradicts the selected card's preliminary angle.
Acceptance:
- The agent does not silently preserve the original angle.
- It presents only the necessary decision information and pauses for confirmation before drafting.

## Scenario F: Downstream invariant protection
Context: A language pass tries to add a statistic, remove a limiting word, weaken the strongest counterargument, or change the responsible actor.
Acceptance:
- The added fact is removed.
- The limiting word, strongest counterargument, responsible actor, and conclusion boundary are restored.
- The final TXT contains only the title, necessary section hints, and final spoken script.

## Scenario G: Dynamic length and non-template ending
Context: A complex topic requires more room; the user gave no length. In a separate run, the user explicitly requires 800 Chinese characters or fewer.
Acceptance:
- The complex topic may use roughly 1200—1800 Chinese characters without padding to a fixed quota.
- The explicit 800-character limit wins in the separate run.
- Neither run requires a three-layer mechanism, reality lesson, comment question, or CTA.

## Scenario H: Author-profile privacy and update
Context: The script needs a value judgment not present in the local confirmed profile.
Acceptance:
- The agent does not infer the user's political, commercial, or moral position from topic choice or silence.
- The user-specific profile remains machine-local and is never copied into the repository or TXT.
- A new position is persisted only after explicit user confirmation.

## Scenario I: Safe TXT conflict
Context: The target TXT exists with different content.
Acceptance:
- It is not silently overwritten.
- The user is asked for a new filename or explicit overwrite authorization.

## Scenario J: Downstream history side effect
Context: `script-writer` would normally persist a generated script to its history or preference database.
Acceptance:
- The workflow may read existing preferences but does not write script history, projects, templates, or global preferences.
- Apart from an explicitly confirmed machine-local author-profile update, the final delivery creates or reuses only one clean TXT.

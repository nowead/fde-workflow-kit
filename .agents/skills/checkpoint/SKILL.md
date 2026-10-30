---
name: checkpoint
description: Use when a planned time checkpoint arrives, a slice runs past its estimate, the human reports remaining time, the work may already be good enough to finish early, or a new feature is about to start in the final hour of a timed task.
---

# Checkpoint

The time left and the value at stake decide the scope. Keep the workspace submittable at all times. Finishing early is a valid outcome.

## Steps

1. Read the clock (default `TZ=KST-9 date +%H:%M`). Take D and the wrap-up deadline W from `docs/progress.md`. If the human gives a different remaining time, reset D from it, keep the same gap between W and D, and update progress.md.
2. From progress.md, requirements.md, and the git log, count the Musts that are PASS, in progress, or not started. Do not re-audit.
3. Decide using the first rule that applies:

| Situation | Decision |
| --- | --- |
| Every Must is PASS (or accepted as a limitation) | **Finish early:** run `$wrapup` now. Offer a Should only if it is small (15 min or less), clearly adds value to the golden path, and is low risk. The human decides. |
| 10 min or less to D | Stop editing code, commit, and hand over for submission. |
| At or past W (D-40 for a 3-hour task) | **Feature freeze:** run `$wrapup`. New features become next steps, unless the human explicitly insists after hearing the time cost. |
| A slice is 50% over its estimate | Cut it to the smallest version that passes its acceptance check. |
| Otherwise | Continue the Musts in golden-path order. Should/Could work starts only after every Must is PASS. |

4. **Stuck rule.** If one problem shows no progress for 10 minutes:
   - Commit or stash the attempt.
   - Return those files to the last good commit.
   - Record the limitation.
5. **Record the decision** as a log line in progress.md. If a Must was cut or the scope changed materially, write an ADR.

## Output

Reply in 6 lines or fewer, in this shape:

```text
남은 시간 1:30 (마감 13:00) | Must 4/4 PASS
결정: 조기 마무리. $wrapup 진행
선택지: 장비별 비교 (Should, 약 15분, 골든 패스와 무관) → 권장하지 않음
다음 행동: $wrapup
```

## Boundaries

The human makes the final call; your job is to make the time cost explicit. Do not change code during the checkpoint itself. The hard rules in AGENTS.md apply.

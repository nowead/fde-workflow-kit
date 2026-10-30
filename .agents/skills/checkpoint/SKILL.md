---
name: checkpoint
description: Use when a planned time checkpoint arrives, a slice runs past its estimate, the human reports remaining time, the work may already be good enough to finish early, the wrap-up point arrives with a Must not yet PASS, or a new feature is about to start in the final hour of a timed task.
---

# Checkpoint

The time left and the value at stake decide the scope. Keep the workspace submittable at all times. Finishing early is a valid outcome. The time before the deadline that the final check and submission need is never spent on features.

## Steps

1. Read the clock (default `TZ=KST-9 date +%H:%M`). Take D, the wrap-up point W, and the wrap-up limit L from `docs/progress.md`. If the human gives a different remaining time, reset D from it, keep the same gaps from W and L to D, and update progress.md.
2. From progress.md, the requirements, and the git log, count the Musts that are PASS, in progress, or not started. Do not re-audit.
3. Decide using the first rule that applies:

| Situation | Decision |
| --- | --- |
| Every Must is PASS (or accepted as a limitation) | **Finish early:** run `$wrapup` now. Offer a Should only if it is small (15 min or less), clearly adds value to the golden path, and is low risk. The human decides. |
| 10 min or less to D | Stop editing code, commit, and hand over for submission. |
| At or past L | **Feature freeze:** return any unfinished attempt to the last good commit and run `$wrapup`. |
| At or past W, a Must is not PASS | **Must go/no-go** (next section). |
| A slice is 50% over its estimate | Cut it to the smallest version that passes its acceptance check. |
| Otherwise | Continue the Musts in golden-path order. Should/Could work starts only after every Must is PASS. |

4. **Stuck rule.** If one problem shows no progress for 10 minutes:
   - Commit or stash the attempt.
   - Return those files to the last good commit.
   - Record the limitation.
5. **Record the decision** as a log line in progress.md. If a Must was cut or the scope changed materially, record it as a decision (an ADR in the full layout).

## Must go/no-go

Weigh the points a missing Must costs against the risk of breaking what already works. Take the open Musts one at a time, highest value first:

1. Estimate E: minutes to build **and verify** the smallest version that passes its acceptance check.
2. **Go** only if all three hold:
   - **Fits:** E × 1.5 ≤ L − now.
   - **Revertible:** the current state is committed and the check passes, so a failed attempt is undone in one step. Note that commit.
   - **Contained:** the change leaves the code behind the PASS Musts and the golden path untouched, or the check command covers every Must it touches.
3. **No-go** otherwise: run `$wrapup`. The Must becomes a limitation, with its smallest version as the first next step.
4. On go, build only that Must. If it is not PASS by L, stash the attempt, return to the noted commit, record the limitation, and run `$wrapup`. If it passes before L, repeat from step 1 for the next open Must.

## Output

Reply in 6 lines or fewer, in this shape:

```text
남은 시간 0:40 (마감 13:00, 마무리 한계 12:35) | Must 4/5 PASS
결정: R5 진행. 예상 8분 ×1.5 = 12분 ≤ 한계까지 15분, a1b2c3 check 통과, 기존 Must 코드 미변경
중단 기준: 12:35까지 PASS가 아니면 a1b2c3로 되돌리고 R5는 한계로 기록
다음 행동: R5 슬라이스 시작
```

## Boundaries

The human makes the final call; your job is to make the time cost explicit. Do not change code during the checkpoint itself, and never start or continue feature work past L. The hard rules in AGENTS.md apply.

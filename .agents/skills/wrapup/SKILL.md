---
name: wrapup
description: Use when every Must is PASS or accepted as a limitation, when the wrap-up point arrives (about 20% of the total time before the deadline; D-40 for a 3-hour task) and no open Must is worth finishing, when the wrap-up limit arrives (D-25), or when the human wants to finish and submit a timed task; covers the feature freeze, final audit, final documents, debrief, and submission checklist in one pass.
---

# Wrap-up

One pass from "building" to "ready to submit". Budget about 30 minutes; started at the wrap-up limit L, it has 15: audit 5, documents 5, debrief and checklist 5. Shrink each step when time is short, but never skip the audit or the debrief.

## Steps

1. **Freeze.**
   - If a Must is not PASS and it is still before L, run the Must go/no-go in the `checkpoint` skill first. On go, return to building, and come back here by L.
   - Read the clock (default `TZ=KST-9 date +%H:%M`) and log `[SCOPE] freeze` in `docs/progress.md`.
   - No new features from here on. Missing features become limitations, each with its smallest version as the first next step.
2. **Final audit.** Follow the `audit` skill in final mode: at most 10 minutes, and P0 fixes to existing behavior only.
3. **Final documents** (at most 10 minutes):
   - Requirements: every requirement has its final status and evidence.
   - Decisions: every significant decision is recorded, including scope cuts and conflict resolutions. Check the log in progress.md against the recorded decisions.
   - `docs/progress.md`: close the current state and add this final section:

     ```text
     ## 최종 결과
     - 요약 (3줄)
     - 실행·확인 방법 (이번 세션에 실행한 명령만)
     - 골든 패스 결과
     - 핵심 결정 (ADR 또는 결정 섹션 링크)
     - AI 활용 (맡긴 것, 검증 방법, 바로잡은 것, 사람이 정한 것)
     - 남은 한계와 개선 방향 (우선순위순, 각각 다음 단계)
     ```

   - Task-required documents (for example `PLAN.md` or `COLLABORATION.md`): write them now as concise views of the docs above and `docs/stakeholder.md`, with links. Do not copy whole sections, and never overwrite the task README.
   - Leave no placeholders. Ask the human at most 3 short questions about facts only they know, and write "기록 없음" for the rest. Label reconstructed history "재구성".
4. **Commit** with `docs: final`, including AGENTS.md. The working tree must be clean.
5. **Debrief.** Follow the `debrief` skill.
6. **Submission checklist** for the human, 6 lines or fewer:
   - The required files are at their exact paths.
   - Every editor tab is saved.
   - The check command passes.
   - The final commit SHA.
   - The readiness verdict.
   - Follow the platform's submission steps.

## Boundaries

- Never fabricate history, reasoning, or evidence.
- The hard rules in AGENTS.md apply.
- Only the platform confirms the submission.

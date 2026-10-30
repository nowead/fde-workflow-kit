---
name: wrapup
description: Use when every Must is PASS or accepted as a limitation, when the wrap-up deadline arrives (about 20% of the total time before the deadline; D-40 for a 3-hour task), or when the human wants to finish and submit a timed task; covers the feature freeze, final audit, final documents, debrief, and submission checklist in one pass.
---

# Wrap-up

One pass from "building" to "ready to submit". Budget about 30 minutes. Shrink each step when time is short, but never skip the audit or the debrief.

## Steps

1. **Freeze.**
   - Read the clock (default `TZ=KST-9 date +%H:%M`) and log `[SCOPE] freeze` in `docs/progress.md`.
   - No new features from here on. Missing features become limitations. If one is small, offer it with a time estimate and let the human decide.
2. **Final audit.** Follow the `audit` skill in final mode: at most 10 minutes, and P0 fixes to existing behavior only.
3. **Final documents** (at most 10 minutes):
   - `docs/requirements.md`: every requirement has its final status and evidence.
   - `docs/adr/`: every significant decision has an ADR, including scope cuts and conflict resolutions. Check the log in progress.md against the ADR list.
   - `docs/progress.md`: close the current state and add this final section:

     ```text
     ## 최종 결과
     - 요약 (3줄)
     - 실행·확인 방법 (이번 세션에 실행한 명령만)
     - 골든 패스 결과
     - 핵심 결정 (ADR 링크)
     - AI 활용 (맡긴 것, 검증 방법, 바로잡은 것, 사람이 정한 것)
     - 남은 한계와 개선 방향 (우선순위순, 각각 다음 단계)
     ```

   - Task-required documents (for example `PLAN.md` or `COLLABORATION.md`): write them now as concise views of the docs above, with links. Do not copy whole sections, and never overwrite the task README.
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

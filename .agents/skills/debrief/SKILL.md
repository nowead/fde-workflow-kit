---
name: debrief
description: Use when the human must explain or defend the delivered work to a reviewer, customer, or teammate, typically as the last step of wrap-up.
---

# Debrief

Prepare the human to explain and defend their own work to a reviewer or customer, truthfully and in their own words. You are a tutor, not a ghostwriter.

## Steps

1. **Ground the facts.** Read `docs/requirements.md`, the ADRs, the final section of `docs/progress.md`, `git log --oneline`, and the core source files. Check every claim against the code and cite it as `file:function`.
2. **Find discrepancies first.** Look for places where the docs, README, or plan claim something the code does not do, or the reverse. List these at the top of the briefing.
3. **Write the briefing** in chat, not in a submission file unless the human asks. Use the task language, 60 lines or fewer:
   1. 30초 요약: 무엇을, 누구를 위해, 어떻게 (골든 패스로)
   2. 구조와 데이터 흐름: 핵심 파일 3~5개
   3. 핵심 결정: ADR마다 결정 → 이유 → 버린 대안
   4. 검증: 실행한 것(명령·결과) / 못 한 것
   5. AI 협업: 맡긴 것 / 바로잡은 것 / 사람이 정한 것
   6. 한계와 다음 단계
   7. 리뷰어가 물을 만한 질문 6~8개. 각각 답 뼈대 2~3줄 (결론 → 근거 → 검증 → 한계)
4. **Close** with the 3 files or functions the human should open and read now, and offer to explain any part.

## Rules

- Give bullet skeletons, not essays to memorize.
- If a decision has no recorded reason, say so. Label any reason inferred now as "사후 설명".
- Unverified items stay unverified in the briefing, so the human does not overclaim.
- Remind the human once: if a question's premise differs from the implementation, state the difference first.

## Boundaries

- Do not change code or docs here unless the human asks.

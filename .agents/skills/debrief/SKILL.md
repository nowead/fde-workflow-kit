---
name: debrief
description: Use when the human must explain or defend the delivered work to a reviewer, customer, or teammate, typically during wrap-up, or wants to rehearse answering questions about it.
---

# Debrief

Prepare the human to explain and defend their own work to a reviewer or customer, truthfully and in their own words. You are a tutor, not a ghostwriter.

## Steps

1. **Ground the facts.** Read `docs/requirements.md`, the decisions, the current state and log in `docs/progress.md`, `git log --oneline`, and the core source files. Check every claim against the code and cite it as `file:function`.
2. **Find discrepancies first.** Look for places where the docs, README, or plan claim something the code does not do, or the reverse. List these at the top of the briefing.
3. **Write the briefing** in chat, not in a submission file unless the human asks. Use the task language, 60 lines or fewer:
   1. 30초 요약: 무엇을, 누구를 위해, 어떻게 (골든 패스로)
   2. 구조와 데이터 흐름: 핵심 파일 3~5개
   3. 핵심 결정: 결정마다 결정 → 이유 → 버린 대안
   4. 검증: 실행한 것(명령·결과) / 못 한 것
   5. AI 협업: 맡긴 것 / 바로잡은 것 / 사람이 정한 것
   6. 한계와 다음 단계
   7. 리뷰어가 물을 만한 질문 6~8개. 각각 답 뼈대 2~3줄 (결론 → 근거 → 검증 → 한계)
4. **Close** with the 3 files or functions the human should open and read now, then the rehearsal offer: `예상 질문으로 연습할까요? "연습"이라고 하면 하나씩 묻겠습니다.` In wrap-up, the offer comes after the submission checklist instead.

## Rehearsal

When the human says "연습":

1. Ask one question per turn, as a reviewer would, with no hints. Use questions the briefing did not cover. Make the first or the second rest on a false premise about the implementation.
2. Wait for the human's own answer. Then reply in 4 lines or fewer: what was right, what was missing or wrong with `file:function`, and the next question.
3. Stop when the human says so. Never answer a question before the human has tried it.

## Rules

- Give bullet skeletons, not essays to memorize.
- If a decision has no recorded reason, say so. Label any reason inferred now as "사후 설명".
- Unverified items stay unverified in the briefing, so the human does not overclaim.
- Remind the human once: if a question's premise differs from the implementation, state the difference first.

## Boundaries

- Do not change code or docs here unless the human asks.

---
name: debrief
description: Use when the human must explain or defend the delivered work to a reviewer, customer, or teammate, typically during wrap-up, or wants to rehearse answering questions about it.
---

# Debrief

Prepare the human to explain and defend their own work to a reviewer or customer, truthfully and in their own words. You are a tutor, not a ghostwriter.

## Steps

1. **Ground the facts.** Read `docs/requirements.md`, the decisions, the current state and log in `docs/progress.md`, `git log --oneline`, and the core source files. Check every claim against the code and cite it as `file:function`.
2. **Find discrepancies first.** Look for places where the docs, README, or plan claim something the code does not do, or the reverse. List these at the top of the briefing.
3. **Write the briefing** in chat, not in a submission file unless the human asks. Use the task language, 70 lines or fewer:
   1. 30초 요약: 무엇을, 누구를 위해, 어떻게 (골든 패스로)
   2. 구성과 흐름: 골든 패스 한 번의 호출 흐름(입력 → 처리 → 저장 → 응답, 단계마다 `file:function`), 상태가 저장되는 곳, 검증과 오류 처리가 일어나는 곳
   3. 핵심 숫자: 과제가 내놓는 결과 숫자(합계, 건수, 금액 등)마다 값 → 공식 → `file:function`. 값은 실행 출력(`[VERIFY]` 기록이나 지금 실행한 명령)에서만 가져오고, 없으면 "미확인". 숫자가 없는 과제면 생략
   4. 핵심 결정: 결정마다 결정 → 이유(관련 R) → 버린 대안 → 감수한 것
   5. 검증: 실행한 것(명령·결과) / 못 한 것
   6. AI 협업: 도구 구성과 역할(AGENTS.md, 쓴 스킬, 세션 분리) / 맡긴 것 / 바로잡은 것 / 사람이 정한 것
   7. 한계: 만들지 못한 것 / 일부러 넣지 않은 것과 이유 / 만든 기능이 깨지는 조건(동시 요청, 재시작, 큰 입력, 잘못된 데이터 중 해당하는 것)과, 요구 범위 밖이라 막지 않았다면 그 근거(R이나 담당자 답). 각각 다음 단계
   8. 리뷰어가 물을 만한 질문 6~8개. 각각 답 뼈대 2~3줄 (결론 → 근거 → 검증 → 한계). "이 규칙이 바뀌면 어디를 고치나"와 "언제 깨지나"를 하나씩 포함
4. **Close** with the 3 files or functions the human should open and read now, then the rehearsal offer: `예상 질문으로 연습할까요? "연습"이라고 하면 하나씩 묻겠습니다.` In wrap-up, the offer comes after the submission checklist instead.

## Rehearsal

When the human says "연습":

1. Ask one question per turn, as a reviewer would, with no hints. Use questions the briefing did not cover. Make the first or the second rest on a false premise about the implementation. Phrase questions in general software terms (컴포넌트 흐름, 상태, 검증 위치), and ask one about a result number if the task produced any.
2. Wait for the human's own answer. Then reply in 4 lines or fewer: what was right, what was missing or wrong with `file:function`, and the next question.
3. Stop when the human says so. Never answer a question before the human has tried it.

## Rules

- Give bullet skeletons, not essays to memorize.
- If a decision has no recorded reason, say so. Label any reason inferred now as "사후 설명".
- Unverified items stay unverified in the briefing, so the human does not overclaim.
- Remind the human once: if a question's premise differs from the implementation, state the difference first.

## Boundaries

- Do not change code or docs here unless the human asks.

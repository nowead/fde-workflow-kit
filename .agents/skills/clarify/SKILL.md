---
name: clarify
description: Use when requirements are ambiguous, missing, or conflicting; when preparing questions for a stakeholder or business owner that the human relays (for example a messenger contact); when the human pastes a stakeholder's reply; or when a finished slice should be shown to the stakeholder for confirmation.
---

# Clarify

You cannot reach the stakeholder; the human relays every message. Ask only what changes what gets built, and turn every answer into a traceable requirement or decision.

## Questions or confirmation

- Ask at most 5 questions, highest impact first.
- Each question names the decision point, gives 2-3 options, and states the default you will use if it goes unanswered.
- Skip anything the README already answers, and anything the team decides itself.
- Once a golden-path slice works, prefer a one-line confirmation over abstract questions:
  `현재 …까지 동작합니다. …는 …로 처리했는데 맞을까요?`
- Output one paste-ready block in the stakeholder's language, in a polite business tone.
- Log it in `docs/progress.md` as `HH:MM [STAKEHOLDER]`.

## Recording a reply

1. **Quote** the reply verbatim, with the time, in the Q&A section of `docs/requirements.md`. Add a log line to progress.md.
2. **Requirements.**
   - Answered items become CONFIRMED (source: 담당자 HH:MM).
   - New rules get new IDs and acceptance checks.
   - Update the golden path if the reply changes it.
3. **Conflicts.** For each conflict with the README or an earlier answer, print this line and ask the human to choose:
   `CONFLICT: README §… says X / 담당자 says Y → 제안: …`
   - Apply neither side until the human chooses.
   - When the human chooses, write an ADR: the decision, who chose it, why, and the source quotes.
4. **Gaps.** For decisions the reply leaves open, implement the stated default, mark it ASSUMED, and add it to the next question batch.
5. **Keep moving.** Update the slice table, then continue with the next slice that no open CONFLICT blocks, unless the human asked you to wait.

## Reply

Keep the reply to 10 lines or fewer, plus any paste-ready blocks, in this order:

1. 확정
2. CONFLICT와 선택지
3. 가정으로 진행하는 것
4. 슬라이스 변경
5. 지금 하는 일

## Boundaries

- Never invent answers.
- Never present a paraphrase as a quote.
- Never mark ASSUMED as CONFIRMED without a quote.
- The hard rules in AGENTS.md apply.

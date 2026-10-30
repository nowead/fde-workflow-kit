---
name: clarify
description: Use when the human has written or pasted a conversation with the stakeholder or business owner into docs/stakeholder.md or the chat, when requirements are ambiguous, missing, or conflicting, or when a finished slice should be confirmed with the stakeholder.
---

# Clarify

The human talks to the stakeholder in their own words and keeps the conversation in `docs/stakeholder.md`. Turn it into requirements the human can check at a glance, then stop so they can review them.

## Files

- `docs/stakeholder.md` is the human's. Read it; never edit, reformat, or save it (it may be open in their editor).
- `docs/requirements.md` is yours. Cite the conversation there; never copy it.
- `docs/progress.md` records how far you have read, as `HH:MM [STAKEHOLDER] stakeholder.md 4-15행 반영: …`.

## Steps

1. **Read only the new lines:** from the line after the range in the last `[STAKEHOLDER]` log line, or from line 1 if there is none. Read the whole file if it is now shorter than that range. If the conversation came in the chat instead, cite it as `채팅 HH:MM`.
2. **Cite by line.**
   - A stakeholder statement: `담당자 12행 "<핵심 구절>"`, quoting only the few words that carry the rule.
   - A line the human marks as a summary, or any line not in the stakeholder's own words, is the human's account: `12행 요약`, without quotation marks.
   - Both are valid sources for CONFIRMED.
3. **Update requirements.md.**
   - New or refined rules become requirement rows: CONFIRMED (source), with an acceptance check the check command can run. Update the golden path if it changes.
   - Remove answered 확인할 것 items; the answer now lives in a requirement row.
   - A conflict with the README or an earlier answer goes in the 충돌 section as `C1: README … "X" / 담당자 12행 "Y" → 제안: …`. Mark the affected rows with the conflict ID and apply neither side until the human chooses.
   - Add 확인할 것 items for what the answers leave open that would change the build: the boundaries and exceptions of each rule (for example, whether an end time equal to the next start counts as overlap), the states a rule creates, and how a rule treats the provided data.
   - Each item is one line with a single question: `Q7 <질문> | 왜: <바뀌는 것> | 기본값: <답이 없을 때>`. Keep existing IDs and number new items after the highest.
   - Keep at most 7 open items, most important first. Settle the rest yourself: write the default into the requirement row as ASSUMED.
4. **Log** one `[STAKEHOLDER]` line in progress.md with the line range and what changed. Update its current state, then commit the docs.
5. **Stop.** Do not start or continue building in this turn. The human reviews requirements.md first.

## When the human answers

- **A conflict choice:** record it as a decision (an ADR in the full layout, the 결정 section in the compact one) with who chose, why, and both quotes. Apply it to the rows and remove the conflict line.
- **"진행" or any go-ahead:** update the slice table and continue with the next slice that no open conflict blocks. Where a slice depends on an open 확인할 것 item, build its 기본값 and mark that requirement `ASSUMED (Q7 기본값)`.

## After a golden-path slice works

Add a 확인할 것 item the human can show the stakeholder: `Q9 동작 확인: <보여 줄 흐름> → <맞는지 물을 것>`.

## Report

10 lines or fewer, in this order:

1. 반영: stakeholder.md N-M행
2. 확정·변경: R… (one line each)
3. 충돌: C… 선택지와 제안
4. 새로 확인할 것: the top 3 Q items
5. `requirements.md를 확인하고 충돌을 골라 주세요. "진행"이라고 하면 이어서 구현합니다.`

## Boundaries

- Questions for the stakeholder exist only as 확인할 것 items; the human asks them in their own words.
- Never invent answers, and never present a summary as a quote.
- Mark a requirement CONFIRMED only with a line in stakeholder.md, the chat, or the README as its source.
- The hard rules in AGENTS.md apply.

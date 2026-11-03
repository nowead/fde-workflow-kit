# AGENTS.md

Working agreement for this workspace.

**Priority:** task README, provided files, and organizer rules > this file > skills. This ranks instructions, not business answers: a stakeholder answer that differs from the README is a conflict the human resolves.

**Language:** write every reply and document in the task's language (Korean unless the task uses another).

## Hard rules

- Never edit the task README, provided data, or provided tests. When the task builds on provided code (a skeleton, starter code, or code to fix), change that code in place. Deliverable names, paths, and formats follow the task.
- Commit locally only. No `git push`, no remotes, and no uploads or other external transfers.
- No computer-use, browser-use, or other GUI or browser automation. The human checks the UI in the Browser preview.
- Do not change approval, sandbox, or platform settings, and do not update Codex.
- Keep secrets, tokens, and passwords out of code, logs, and docs.
- Borrow external code only in small parts, and cite the source in `docs/progress.md`. Never replace the deliverable wholesale.

## Slice loop

1. Build one thin vertical slice (10-25 min), in golden-path order, with a test of its acceptance check named after the requirement ID and rule (for example `test_R6_end_equal_to_next_start_is_allowed`).
2. Run the check command (see "Verified commands"). "Done" means it passed with the slice's test included; anything you did not check is UNVERIFIED.
3. Update the docs (next section).
4. Commit the code and docs together, with a message that names the requirement IDs and says what changed and why.
5. Send the slice report (see "Replies").

Web servers bind `0.0.0.0` on a fixed port.

## Docs: the record of the work

`$kickoff` sizes the record to the task and notes the layout in progress.md. Either way it holds requirements with status and verification results, decisions with their reasons, and the log.

- `docs/requirements.md`: the purpose (problem, success criteria, golden path, deliverables), requirements, conflicts, and 확인할 것 (questions for the stakeholder, each with why it matters and a default). Give each requirement a status (CONFIRMED with its source, ASSUMED, or OPEN) and its verification result. Update it whenever a requirement or status changes.
- `docs/stakeholder.md`: the human's own record of the stakeholder conversation. Read it; never edit it.
- `docs/adr/NNNN-title.md`: one file per significant decision, at most 15 lines. Significant means the stack, data, a rule interpretation, a conflict resolution, or a scope cut. Each file covers context, options, the decision, its consequences, and the source. When the human made the call, the source is their own words: `사람: "…"`.
- `docs/progress.md`: the current state (a new session reads this first), the slice table, and a timestamped log of stakeholder exchanges, the human's calls in their own words, AI delegations and corrections, and verification results.

Compact layout (small tasks): no `docs/adr/`. The 결정 section of requirements.md stands in wherever this file or a skill names an ADR.

Task-required documents (for example `PLAN.md`) start at kickoff as short views that link to these docs, change when the plan changes, and are finished at wrap-up. Never maintain duplicates.

## Replies

After each slice, reply in this shape (the 미리보기 line only when the slice changed a screen):

```text
남은 시간 1:20 | 슬라이스 3 R4 PASS (check 14/14) | 커밋 a1b2c3
읽을 곳: <file:function> - <what it does and why, with the requirement ID>
미리보기: <port/path> → <what to click and expect>
가정·결정: <ASSUMED defaults or decisions this slice used, or 없음>
다음: 슬라이스 4 - <name> (<estimate>분)
```

Other replies give the time left first, then the result, then the next step. Skills set their own report shapes.

- Read the clock in the human's time zone (default `TZ=KST-9 date +%H:%M`).
- Spend tokens deliberately: read only what you need, and never print whole large files or logs.

## Subagents

Only when a subagent tool (such as `spawn_agent`) is already available, and only for read-only work: mapping a provided codebase too large to read whole, or an independent review of the finished Musts against `docs/requirements.md` in the final audit. Give it a clean context (`fork_turns: "none"` where offered) and a self-contained brief, leave its model unset, and let it edit nothing. Confirm its findings before acting on them, and log an `[AI]` line.

## Finishing (there is no minimum time)

Run `$wrapup` as soon as every Must is PASS or accepted by the human as a limitation, however much time is left.

- At the wrap-up point W (about 20% of the total time before the deadline; D-40 for a 3-hour task), run `$checkpoint`. If a Must is still open, it weighs whether that Must can be built and verified before L without risking what already works; otherwise it runs `$wrapup`.
- Start `$wrapup` by the wrap-up limit L (D-25) no matter what. The final check and submission time is never spent on features.

The work is done when all three hold:

- The final audit in `$wrapup` says READY or READY WITH RISKS.
- The docs are current.
- The human can explain the work.

## Skills

- `$kickoff`: start or resume
- `$clarify`: turn the stakeholder conversation into requirements
- `$checkpoint`: time and scope
- `$audit`: evidence check
- `$wrapup`: freeze, final audit, debrief, final docs
- `$debrief`: brief the human and rehearse their answers

## Verified commands (only commands actually run)

- Install:
- Run:
- Check:
- Preview: port / path

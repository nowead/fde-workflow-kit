# AGENTS.md

Working agreement for this workspace.

**Priority:** task README, provided files, and organizer rules > this file > skills.

**Language:** write every reply and document in the task's language (Korean unless the task uses another).

## Hard rules

- Never edit the task README or provided files. Deliverable names, paths, and formats follow the task.
- Commit locally only. No `git push`, no remotes, and no uploads or other external transfers.
- No computer-use, browser-use, or other GUI or browser automation. The human checks the UI in the Browser preview.
- Do not change approval, sandbox, or platform settings, and do not update Codex.
- Keep secrets, tokens, and passwords out of code, logs, and docs.
- Borrow external code only in small parts, and cite the source in `docs/progress.md`. Never replace the deliverable wholesale.

## Slice loop

1. Build one thin vertical slice (10-25 min), in golden-path order.
2. Run the check command (see "Verified commands"). "Done" means it passed; anything you did not check is UNVERIFIED.
3. Update the docs (next section).
4. Commit the code and docs together, with a message that says what changed and why.

Web servers bind `0.0.0.0` on a fixed port. Tell the human the port and path for the Browser preview.

## Docs: the record of the work

`$kickoff` sizes the record to the task and notes the layout in progress.md. Either way it holds requirements with status and verification results, decisions with their reasons, and the log.

- `docs/requirements.md`: the purpose (problem, success criteria, golden path, deliverables), requirements, conflicts, and 확인할 것 (questions for the stakeholder, each with why it matters and a default). Give each requirement a status (CONFIRMED with its source, ASSUMED, or OPEN) and its verification result. Update it whenever a requirement or status changes.
- `docs/stakeholder.md`: the human's own record of the stakeholder conversation. Read it; never edit it.
- `docs/adr/NNNN-title.md`: one file per significant decision, at most 15 lines. Significant means the stack, data, a rule interpretation, a conflict resolution, or a scope cut. Each file covers context, options, the decision, its consequences, and the source.
- `docs/progress.md`: the current state (a new session reads this first), the slice table, and a timestamped log of stakeholder exchanges, AI delegations and corrections, and verification results.

Compact layout (small tasks): no `docs/adr/`. The 결정 section of requirements.md stands in wherever this file or a skill names an ADR.

Write task-required documents from these at wrap-up; never maintain duplicates.

## Replies

- Keep replies to 10 lines or fewer unless a skill defines a longer output or the human asks for more. Put the time left first, then the result, then the next step.
- Read the clock in the human's time zone (default `TZ=KST-9 date +%H:%M`).
- Spend tokens deliberately: read only what you need, and never print whole large files or logs.
- Use subagents only when the human asks, and only for independent work with no shared files.

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
- `$wrapup`: freeze, final audit, final docs, debrief
- `$debrief`: prepare the human to explain and defend the work

## Verified commands (only commands actually run)

- Install:
- Run:
- Check:
- Preview: port / path

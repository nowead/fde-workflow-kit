---
name: kickoff
description: Use when a time-boxed assignment starts in a new or unfamiliar workspace, or when resuming in a fresh, compacted, or restarted session that must recover task state from docs/progress.md.
---

# Kickoff

Make the task executable in about 15 minutes, then start building. Nothing speculative gets built.

## Resume mode

Use this mode if `docs/progress.md` exists or the human says 복구/resume:

1. Read only its "현재 상태" section, `git log --oneline -15`, and `git status`.
2. Reply in 3 lines: where we are, the next step, and the time left.
3. Continue. Do not re-read the whole task.

## Steps

1. **Clock.** Read the clock in the human's time zone (default `TZ=KST-9 date +%H:%M`, which works without tzdata; sandbox clocks are often UTC).
   - Deadline D = now + the remaining time the human gave. If they gave none, ask once.
   - Wrap-up deadline W = D minus a fifth of the remaining time, with that amount rounded up to the next 10 minutes (D-40 for a 3-hour task). Submit by D-10.
   - Target finish = your estimate of Musts plus wrap-up, if that comes before D-10.
2. **Read** the task README and every provided file. Check sizes first and use `head` on large data. Never edit these files.
3. **Frame the problem** before listing features: whose problem it is, what hurts today, and what success looks like.
   - Then pick the golden path: the 2-3 minute end-to-end user flow that must work.
   - The golden path sets the slice order, the smoke check, the preview check, and the final story.
4. **Requirements.** Create `docs/requirements.md` from `templates.md` in this folder. It covers:
   - the problem, success criteria, and golden path
   - deliverables with exact paths, citing the README section
   - Must/Should/Could requirements, each with status CONFIRMED (source), ASSUMED, or OPEN
   - open questions and out-of-scope items
5. **Stack.** Prefer what the environment already has. Add dependencies only when a Must needs them. Record the choice in `docs/adr/0001-<stack>.md`. Web servers bind `0.0.0.0` on a fixed port.
6. **Check command.** Create one command that runs the tests plus a golden-path smoke check and exits non-zero on failure (for example `scripts/check.sh` or `npm run check`). Run it once now.
7. **Git.** If `git status` fails, run `git init` and commit the provided files as the baseline. Commit locally only.
8. **Progress.** Create `docs/progress.md` from the template with:
   - the current state, D, target finish, and W
   - the slice table: 10-25 minutes per slice, golden path first, Musts before Shoulds. Slice 1 must not depend on open questions.
   - the first log line
9. **AGENTS.md.** Fill "Verified commands" with commands you actually ran. If the task names other doc files, add one line saying which task file each doc feeds.
10. **Questions.** Draft at most 5 stakeholder questions, highest impact first.
    - Each question names the decision point, gives 2-3 options, and states the default you will use if it goes unanswered.
    - Never ask what the README answers, or what the team decides itself (stack, structure).
    - Write a paste-ready block in the stakeholder's language and a polite business tone.
11. **Commit** with `chore: kickoff` (docs, check command, AGENTS.md), then send the report.

## Report

Keep it to 10 lines or fewer plus the question block:

```text
남은 시간 2:50 | 마감 13:00 | 목표 종료 12:30 | 늦어도 마무리 12:20
문제·성공: …
골든 패스: … → … → …
산출물: <exact paths> (README §…)
check: <command> → <result>
업무 담당자 질문 (그대로 복사해 보내세요):
<block>
지금 직접 확인할 것: <README 구간 등>
다음: 슬라이스 1 - … (지금 시작)
```

## After the report

Start slice 1 in the same turn unless the human asked you to wait. Until the stakeholder answers, build nothing an open question could change. Add no persistence layers, fuzz tests, or extra tooling unless a Must requires them.

## Boundaries

The task README and organizer rules override this skill. Never invent requirements or answers. The hard rules in AGENTS.md apply. If AGENTS.md is missing, still never push, use GUI automation, or change platform settings.

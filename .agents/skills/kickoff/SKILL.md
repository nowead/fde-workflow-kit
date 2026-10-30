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

1. **Clock.** Read the clock in the human's time zone (default `TZ=KST-9 date +%H:%M`; sandbox clocks are often UTC).
   - Deadline D = now + the remaining time the human gave. If they gave none, ask once.
   - Wrap-up point W = D minus a fifth of the remaining time, rounded up to 10 minutes (D-40 for 3 hours). `$checkpoint` decides on open Musts there.
   - Wrap-up limit L = D-25 (or W, if later): 15 minutes of short wrap-up plus 10 to submit; no feature work crosses it. Submit by D-10.
   - Target finish = estimated Musts plus wrap-up, if before D-10.
2. **Read** the task README and every provided file. Check sizes first and use `head` on large data. Never edit these files.
3. **Frame the problem** before listing features: whose problem it is, what hurts today, and what success looks like.
   - Then pick the golden path: the 2-3 minute end-to-end flow that must work.
   - It sets the slice order, smoke check, preview check, and final story.
4. **Requirements.** Write `docs/requirements.md` from `templates.md` here:
   - The purpose (problem, success, golden path, deliverables) and the README's requirements, each CONFIRMED (source), ASSUMED, or OPEN.
   - 확인할 것: what the README leaves to the stakeholder and gaps that would change the build (rule boundaries and exceptions, states in the provided data). At most 7 one-line items, each one question with why and a default, most important first.
   - Create `docs/stakeholder.md` from its template; it is the human's, so never edit it afterwards.
   - Layout: compact (3 or fewer Musts, no decision records required) keeps decisions in the 결정 section of requirements.md; full adds `docs/adr/`.
5. **Stack.** Prefer what the environment has; add dependencies only for a Must. Record it as decision 1 (`docs/adr/0001-<stack>.md` when full); a fixed stack needs only a log line. Web servers bind `0.0.0.0` on a fixed port.
6. **Check command.** One command that runs the tests plus a golden-path smoke check and exits non-zero on failure (for example `scripts/check.sh`). Run it once now.
7. **Git.** If `git status` fails, run `git init` and commit the provided files as the baseline. Commit locally only.
8. **Progress.** Complete `docs/progress.md` from the template with:
   - the layout, the current state, D, target finish, W, and L
   - the slice table: 10-25 minutes per slice, golden path first, Musts before Shoulds. Slice 1 must not depend on open questions.
   - the first log line
9. **AGENTS.md.** Fill "Verified commands" with commands you actually ran. If the task names other doc files, note which task file each doc feeds.
10. **Commit** with `chore: kickoff` (docs, check command, AGENTS.md), then send the report.

## Report

Keep it to 10 lines or fewer:

```text
남은 시간 2:50 | 마감 13:00 | 목표 종료 12:30 | 마무리 판단 12:20 | 한계 12:35
문제·성공: …
골든 패스: … → … → …
산출물: <exact paths> (README §…), 기록: 압축/전체
check: <command> → <result>
담당자에게 확인할 것: requirements.md Q1-Qn (먼저: Q1 …, Q2 …)
대화는 docs/stakeholder.md에 붙여 넣고 $clarify
지금 직접 확인할 것: <README 구간 등>
다음: 슬라이스 1 - … (지금 시작)
```

## After the report

Start slice 1 in the same turn unless the human asked you to wait. Build nothing an open 확인할 것 item could change. Add no persistence layers, fuzz tests, or extra tooling unless a Must requires them.

## Boundaries

The task README and organizer rules override this skill. Never invent requirements or answers. The hard rules in AGENTS.md apply. If AGENTS.md is missing, still never push, use GUI automation, or change platform settings.

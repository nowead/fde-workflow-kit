---
name: kickoff
description: Use when a time-boxed assignment starts in a new or unfamiliar workspace, or when resuming in a fresh, compacted, or restarted session that must recover task state from docs/progress.md.
---

# Kickoff

Make the task executable in about 15 minutes, then build. Nothing speculative gets built.

## Resume mode

Use this mode if `docs/progress.md` exists or the human says 복구/resume:

1. Read its 현재 상태, the 요구사항 table and 충돌 section of `docs/requirements.md`, `git log --oneline -15`, and `git status`. Do not re-read the task.
2. Reply in 3 lines: where we are, next step, time left.
3. Start that step in this turn, applying the human's corrections. Stop and ask instead if 현재 상태 waits for a human reply, or if `git status` shows uncommitted changes besides `docs/stakeholder.md` (list them).

## Steps

1. **Clock.** Read the clock in the human's time zone (default `TZ=KST-9 date +%H:%M`).
   - Deadline D = now + the remaining time the human gave; if none, ask once.
   - Wrap-up point W = D minus a fifth of the remaining time, rounded up to 10 minutes (D-40 for 3 hours).
   - Wrap-up limit L = D-25 (or W, if later); no feature work crosses it. Submit by D-10.
   - Target finish = estimated Musts plus wrap-up, if before D-10.
2. **Read** the task README and every provided file. Check sizes first; use `head` on large data.
3. **Frame the problem** before listing features: whose problem it is, what hurts today, and what success looks like.
   - Then pick the golden path: the 2-3 minute end-to-end flow that must work.
   - It sets the slice order, smoke check, preview check, and final story.
4. **Requirements.** Write `docs/requirements.md` from `templates.md` here:
   - The purpose (problem, success, golden path, deliverables) and the README's requirements, each CONFIRMED (source), ASSUMED, or OPEN.
   - 확인할 것: first the context the README leaves out (who uses it, how it is done today, what matters most), then gaps that would change the build (rule boundaries and exceptions, who may perform each action even without login, states in the provided data). Up to 7 items (one-line question, why, default), context first, then by importance.
   - Create `docs/stakeholder.md` from its template; never edit it afterwards.
   - Layout: compact (3 or fewer Musts, no decision records required) keeps decisions in the 결정 section of requirements.md; full adds `docs/adr/`.
   - Tell the human at once: `담당자에게 확인할 것 준비됨: docs/requirements.md Q1-Qn (먼저: Q1 …)` and `대화는 docs/stakeholder.md에 붙여 넣고 $clarify`.
5. **Stack.** Prefer what the environment has; add dependencies only for a Must, and install them now, while the human can approve. Record it as decision 1 (`docs/adr/0001-<stack>.md` when full); a fixed stack needs only a log line. Web servers bind `0.0.0.0` on a fixed port.
6. **Check command.** One command that runs the tests plus a golden-path smoke check and exits non-zero on failure (e.g. `scripts/check.sh`). Run it once now.
7. **Git.** If `git status` fails, run `git init` and commit the provided files as the baseline.
8. **Progress.** Complete `docs/progress.md` from the template with:
   - the layout, the current state, D, target finish, W, and L
   - the slice table: 10-25 minutes per slice, golden path first, Musts before Shoulds. Slice 1 must not depend on open questions.
   - the first log line
9. **AGENTS.md and task documents.** Fill "Verified commands" with commands you actually ran. Create each document the task requires (e.g. `PLAN.md`) now, as a short view from `templates.md`.
10. **Commit** with `chore: kickoff` (docs, task documents, check command, AGENTS.md), then send the report.

## Report

Keep it to 10 lines or fewer, ending with the 확인 line:

```text
남은 시간 2:50 | 마감 13:00 | 목표 종료 12:30 | 마무리 판단 12:20 | 한계 12:35
문제·성공: …
골든 패스: … → … → …
산출물: <exact paths> (README §…), 기록: 압축/전체
스택: … (결정 1: <이유 한 줄>)
check: <command> → <result>
담당자에게 확인할 것: requirements.md Q1-Qn (먼저: Q1 …) → 대화는 docs/stakeholder.md에 붙여 넣고 $clarify
다음: 슬라이스 1 - … (지금 시작)
확인: README §…와 대조해 문제·골든 패스·스택이 맞으면 이유 한 줄, 다르면 고칠 점
```

## After the report

Start slice 1 in the same turn, without waiting for the 확인 answer, unless the human asked you to wait. Build nothing an open 확인할 것 item could change. Add no persistence layers, fuzz tests, or extra tooling unless a Must requires them.

Log the 확인 answer as `사람: "…"`; if it changes the framing or stack, update the docs and slices first.

## Boundaries

The task README and organizer rules override this skill. Never invent requirements or answers. The hard rules in AGENTS.md apply. If AGENTS.md is missing, still never push, use GUI automation, change platform settings, or edit the README, provided data, or provided tests.

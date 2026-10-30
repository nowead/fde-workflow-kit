---
name: audit
description: Use when an implementation slice needs more verification than the check command, before final submission, or whenever anyone claims something is done, fixed, or working and it must be checked against acceptance criteria with real execution evidence.
---

# Audit

Prove what works. Never infer it from code or from claims.

## Modes

- `quick` (about 5 min): check the changed behavior plus the golden path. During building the check command is usually enough; use this mode when a slice touches risky areas.
- `final` (at most 10 min, fixes included): check every requirement and every deliverable. `$wrapup` runs this mode.

## Checks, in risk order

1. **Check and run commands.** The check command passes from the current state, and the run command in AGENTS.md works.
2. **Golden path and Musts.** The golden path works end to end, and each Must passes its acceptance check (tests or `curl`).
3. **Edge cases.** Check invalid input, boundaries, errors, and regressions. Malformed input must get a 4xx response and must never crash the process.
4. **Web apps.**
   - The server binds `0.0.0.0` on the documented port.
   - `curl -s -o /dev/null -w '%{http_code}' http://localhost:PORT/` returns 200.
   - Give the human a 3-step check for the Browser preview: the port and path, what to click, and the expected result.
   - Never use GUI or browser automation, and never claim a UI check you did not observe.
5. **Basics.** Input is validated, output is escaped, and there are no secrets. If an unauthenticated server binds `0.0.0.0`, list the missing auth as a limitation.

Prefer existing tests. Add narrow tests only for uncovered high-risk behavior. Stop any server you start.

## Classify

Give each item one status:
- `PASS`: shown by executed evidence.
- `FAIL`: checked and shown to be wrong.
- `UNVERIFIED`: no evidence yet.
- `NOT_IMPLEMENTED`: the feature is missing.
- `N/A`: does not apply; give the reason.

Never turn UNVERIFIED into PASS.

Set a priority for each problem:
- P0: blocks submission, breaks a Must or the golden path, or lets any input crash the app.
- P1: a Should fails.
- P2: polish.

## Fix

Make the smallest safe fix, rerun the check, and commit with `fix: …`.

With less than 20 minutes to D:
- Fix only P0 defects in behavior that already exists: a crash, a wrong result, the bind address, or a missing required file. Spend at most 5 minutes on each.
- A check that exists but covers only part of its rule counts as a wrong result, so fix it within the same 5 minutes. Example: an overlap check that ignores one of the required keys.
- Do not build NOT_IMPLEMENTED features, meaning features with no code at all. Record them as limitations, and if one is small, offer it to the human with a time estimate.

## Record and report

- Write each status into the verification column of the requirements table.
- Add one `[VERIFY]` line per check to progress.md, in the form command → result.
- Report in 15 lines or fewer:
  - Coverage: counts of each status.
  - Evidence: for the golden path and each Must.
  - Blocking defects: how to reproduce each, and the fix.
  - Residual risks.
  - Readiness: `READY`, `READY WITH RISKS`, or `BLOCKED`, with a one-line basis.

## Boundaries

- Never fabricate tests, outputs, observations, or approvals.
- Never weaken requirements or tests to make them pass.
- The hard rules in AGENTS.md apply.
- Only the platform confirms a submission.

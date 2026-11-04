---
name: explain
description: Use when the human asks what a term, concept, library, error, or part of the workspace code means, or why it was built that way, especially in a second session opened while another session builds.
---

# Explain

Help the human understand the work while it grows, so they can explain it in their own words. You are a tutor, not a ghostwriter. Another Codex session may be building in this same workspace, so answering changes nothing.

## While answering

- Read only what the question needs: the files it names, plus `docs/requirements.md` and `docs/progress.md` for reasons.
- Explain committed code with `git show HEAD:<path>`. If `git --no-optional-locks diff --stat HEAD -- <path>` shows uncommitted changes, read the working copy and say it is still in progress.
- Change nothing: no edits, commits, tests, servers, or installs. Run git only as `git log`, `git show`, or `git --no-optional-locks …`, so you never take the index lock the building session needs.
- In a session the human opened with `$explain`, run no other skill and build nothing; the other session owns the work.

## Answer shape

8 lines or fewer, in the task language.

Something in the code:

```text
뜻: <one plain sentence>
우리 코드: <file:function> - <what it does there> (<R… or D… behind it>)
왜: <the recorded reason, 기록 없음, or 사후 설명: <your inference>>
확인: <one question the human can answer in their own words>
```

Something not in the code:

```text
뜻: <one plain sentence>
우리 코드에는 없음: <where it would fit, why the work does without it, or what would change with it; omit this part if the concept is unrelated to the task>
확인: <one question>
```

When the human answers a 확인 question, reply in 2 lines: what was right, then what was missing or wrong, with `file:function`.

## When you spot a problem

For a bug, a gap, or a choice someone must make, add one line, `구현 세션에 가져갈 것: …`, and fix nothing.

## Boundaries

- Never invent reasons: a reason not in the docs is 기록 없음 or 사후 설명.
- The hard rules in AGENTS.md apply.

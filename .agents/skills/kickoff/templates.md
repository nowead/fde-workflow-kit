# Doc skeletons

Use the task's language for headings and content. Delete sections the task does not need. Final docs contain no placeholders.

Both layouts keep the same content: requirements with status, source, and verification results, decisions with their reasons, and the log.

- **Full:** `docs/requirements.md`, `docs/stakeholder.md`, `docs/adr/`, and `docs/progress.md`.
- **Compact** (3 or fewer Musts, no decision records required): the same without `docs/adr/`. Decisions go in the 결정 section of requirements.md, and wherever a skill names an ADR, use that section. When it passes 3 decisions, move them into `docs/adr/`.

## docs/requirements.md

```markdown
# 요구사항: <과제명>

## 목적
- 누구의 문제: …
- 지금 무엇이 불편한가: …
- 성공의 모습: … (확인할 수 있는 기준)
- 골든 패스 (2~3분 시연): 1. … → 2. … → 3. …
- 산출물: `<path>`: <설명> (README §…)

## 요구사항
| ID | 요구사항 | 우선순위 | 상태 (출처) | 수용 기준 | 검증 |
| --- | --- | --- | --- | --- | --- |
| R1 | … | Must | CONFIRMED (README §2) | … | 미검증 |
| R6 | … | Must | CONFIRMED (담당자 12행 "<핵심 구절>") | … | PASS (`check`) |
| R7 | … | Should | ASSUMED (Q3 기본값) | … | 미검증 |

## 충돌 (사람이 고를 때까지 어느 쪽도 적용하지 않음)
- C1: README §2 "…" / 담당자 12행 "…" → 제안: …

## 확인할 것 (중요한 순, 최대 7개, 한 줄에 질문 하나. 담당자에게 내 말로 묻는다)
- Q1 <질문 하나> | 왜: <바뀌는 것> | 기본값: <답이 없을 때>
- Q5 동작 확인: <보여 줄 흐름> → <맞는지 물을 것>

## 범위 밖
- …

## 결정 (압축 형식에서만. 전체 형식은 docs/adr/)
- D1 HH:MM <결정>: <고른 것>. 이유: … / 버린 대안: … / 출처: README §… 또는 담당자 12행 또는 사람의 결정
```

## docs/stakeholder.md

Kickoff creates only this header. After that the file belongs to the human.

```markdown
# 업무 담당자 대화

담당자와 나눈 대화를 붙여 넣는 곳입니다. 사람만 고치고, Codex는 읽기만 합니다.
직접 요약해서 적은 부분은 앞에 (요약)이라고 표시해 주세요.
```

## docs/adr/NNNN-title.md

```markdown
# ADR-0001: <결정 제목>

- 상태: 채택 (HH:MM) | 대체됨 → ADR-000N
- 출처: README §… / 담당자 12행 "…" / 사람의 결정

## 맥락
<왜 결정이 필요했나. 2~3줄>

## 선택지
1. … : 장점 / 단점
2. … : 장점 / 단점

## 결정
<무엇을 골랐고 왜>

## 결과
- 얻는 것: …
- 감수하는 것: …
```

## docs/progress.md

```markdown
# 진행 상황

## 현재 상태 (갱신 HH:MM)
- 기록 방식: 전체 (requirements.md, stakeholder.md, adr/, progress.md) | 압축 (adr/ 대신 requirements.md 결정 섹션)
- 남은 시간 H:MM | 마감 HH:MM | 목표 종료 HH:MM | 마무리 판단 HH:MM | 마무리 한계 HH:MM
- 단계: 킥오프 / 구현 / 마무리
- 완료(PASS): …
- 진행 중: …
- 다음: …
- 막힌 것·열린 질문: …

## 슬라이스
| # | 슬라이스 | 요구사항 | 예상(분) | 상태 | 커밋 |
| --- | --- | --- | --- | --- | --- |
| 1 | … | R1 | 15 | 진행 중 | |

## 로그
- HH:MM [STAKEHOLDER] stakeholder.md 4-15행 반영: R6·R7 확정, C1 충돌, Q6~Q8 추가
- HH:MM [ADR-0002] 저장 방식: JSON 파일
- HH:MM [AI] 첫 구현이 장비 겹침만 검사함을 테스트로 발견 → 엔지니어 겹침 추가
- HH:MM [VERIFY] `scripts/check.sh` → 12/12 PASS
- HH:MM [SCOPE] R5 진행: 예상 8분 ×1.5 ≤ 한계까지 15분, 되돌릴 커밋 a1b2c3
- HH:MM [SCOPE] 기능 동결
```

# Doc skeletons

Use the task's language for headings and content. Delete sections the task does not need. Final docs contain no placeholders.

## docs/requirements.md

```markdown
# 요구사항: <과제명>

## 문제와 성공 기준
- 누구의 문제: …
- 지금 무엇이 불편한가: …
- 성공의 모습: … (확인할 수 있는 기준)

## 골든 패스 (2~3분 시연 흐름)
1. … → 2. … → 3. …

## 산출물 (과제 지정 경로)
- [ ] `<path>`: <설명> (README §…)

## 요구사항
| ID | 요구사항 | 우선순위 | 상태 (출처) | 수용 기준 | 검증 |
| --- | --- | --- | --- | --- | --- |
| R1 | … | Must | CONFIRMED (README §2) | … | PASS (`check`) |

## 업무 담당자 Q&A (원문 인용)
- HH:MM Q: … / A: "…"

## 열린 질문과 가정
- OPEN: …
- ASSUMED: … (기본값과 근거)

## 범위 밖
- …
```

## docs/adr/NNNN-title.md

```markdown
# ADR-0001: <결정 제목>

- 상태: 채택 (HH:MM) | 대체됨 → ADR-000N
- 출처: README §… / 담당자 HH:MM "…" / 사람의 결정

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
- 남은 시간 H:MM | 마감 HH:MM | 목표 종료 HH:MM | 늦어도 마무리 HH:MM
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
- HH:MM [STAKEHOLDER] 질문 5개 전달 (requirements.md Q&A 참고)
- HH:MM [ADR-0002] 저장 방식: JSON 파일
- HH:MM [AI] 첫 구현이 장비 겹침만 검사함을 테스트로 발견 → 엔지니어 겹침 추가
- HH:MM [VERIFY] `scripts/check.sh` → 12/12 PASS
- HH:MM [SCOPE] 기능 동결
```

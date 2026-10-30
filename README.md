# FDE Workflow Kit

시간 제한이 있는 실무형 AI 코딩 과제를 FDE(Forward Deployed Engineer)처럼 풀기 위한 **Codex 스킬 6개와 AGENTS.md 템플릿**입니다.

FDE처럼 푼다는 것은 이런 흐름입니다. 고객의 문제를 먼저 정의하고, 가장 작은 동작하는 결과를 빨리 만들고, 실행으로 증명하고, 결정과 한계를 기록으로 남깁니다.

이 저장소에는 **작업 방식만** 있습니다. 과제 정답 코드, MCP 서버, 에이전트, 프레임워크 설치 도구는 없습니다.

## 빠른 시작

작업 폴더(과제 README가 있는 곳)의 터미널에서 실행합니다.

```bash
git clone --depth 1 https://github.com/nowead/fde-workflow-kit /tmp/kit && bash /tmp/kit/install.sh .
codex
```

- 스킬은 `~/.agents/skills/`(Codex 사용자 범위)로 복사됩니다. 작업 폴더는 어지럽히지 않습니다.
- `.` 인자를 주면 작업 폴더에 `AGENTS.md`가 **없을 때만** 템플릿을 만듭니다.
- Codex에서 `/skills`나 `$`를 입력해 스킬 6개가 보이는지 확인합니다.
- 설치 스크립트는 파일 복사만 합니다. 네트워크 접속, 패키지 설치, Codex 설정 변경은 하지 않습니다.

| 상황 | 방법 |
| --- | --- |
| 스킬이 안 보임 | Codex 재시작 → 설치 없이 "`/tmp/kit/.agents/skills/kickoff/SKILL.md`를 읽고 따라줘" |
| 작업 폴더 안에 두고 싶음 | `bash /tmp/kit/install.sh . --repo` (`./.agents/skills`, 제출물에 포함됨) |
| 구버전 Codex | `--legacy` (`$CODEX_HOME/skills`에 복사). 제한된 환경에서는 허용 여부를 먼저 확인하세요 |
| git clone 불가 | `curl -L https://github.com/nowead/fde-workflow-kit/archive/refs/heads/main.tar.gz \| tar xz -C /tmp && bash /tmp/fde-workflow-kit-main/install.sh .` |

## 흐름

사람이 칠 명령은 다섯 가지입니다. 단계를 따라가며 이렇게 씁니다.

1. 시작: `$kickoff 남은 시간 2:55`
2. 담당자 답이 오면: `$clarify 업무 담당자 답변: …`
3. 구현 중: "다음 슬라이스: …"
4. 40분마다: `$checkpoint 남은 시간 …`
5. 끝낼 때: `$wrapup`

| 스킬 | 언제 | 하는 일 |
| --- | --- | --- |
| `$kickoff` | 시작할 때, 새 세션에서 이어 갈 때 | 마감과 목표 종료 시각 설정. 문제와 성공 기준, 골든 패스 정의. 문서 3종과 `check` 명령, 담당자 질문을 만든 뒤 바로 슬라이스 1 시작 |
| `$clarify` | 요구사항이 모호할 때, 담당자 답을 붙여넣을 때 | 질문 묶음 작성, 답변 원문 기록, 충돌 표시, 사람이 고르면 ADR, 동작 확인 메시지 |
| `$checkpoint` | 40분마다, 일정이 밀릴 때 | 남은 시간 대비 남은 일 판단. Must가 다 끝났으면 **조기 마무리** |
| `$audit` | `check`보다 깊은 확인이 필요할 때 | 요구사항별 실행 증거, PASS/FAIL/UNVERIFIED, 제출 준비 판정 |
| `$wrapup` | Must가 모두 PASS일 때, 늦어도 전체 시간의 약 20%가 남았을 때(3시간 과제면 D-40) | 동결 → 최종 점검 → 문서 마무리 → 설명 준비 → 제출 체크리스트를 한 번에 |
| `$debrief` | 리뷰어나 고객에게 작업을 직접 설명하고 방어해야 할 때 | 사실 확인을 거친 브리핑, 문서와 구현의 차이, 리뷰어가 물을 만한 질문의 답 뼈대 |

**최소 시간은 없습니다.** Must가 모두 PASS이거나 사람이 한계로 인정하면, 남은 시간과 상관없이 `$wrapup`으로 마무리합니다. 늦어도 전체 시간의 약 20%가 남았을 때(3시간 과제면 D-40) 시작합니다. 남는 시간에 기능을 덧붙이면 토큰, 회귀 위험, 설명해야 할 코드가 모두 늘어나기 때문입니다.

`$wrapup`의 최종 점검이 READY(또는 READY WITH RISKS)이고, 문서가 최신이고, 사람이 작업을 설명할 수 있으면 끝입니다.

## 작업 기록 (작업 공간의 `docs/`)

| 문서 | 내용 |
| --- | --- |
| `docs/requirements.md` | 문제와 성공 기준, 골든 패스, 산출물, 요구사항(상태와 출처, 검증 결과), 담당자 Q&A 원문 |
| `docs/adr/NNNN-*.md` | 중요한 결정 하나당 한 파일: 맥락 → 선택지 → 결정 → 결과 → 출처 |
| `docs/progress.md` | 현재 상태(새 세션은 여기부터 읽음), 슬라이스 표, 시간순 로그(담당자 교신, AI 협업, 검증). 마지막에 최종 결과 |

과제가 다른 문서를 요구하면(예: `PLAN.md`), 마무리 단계에서 이 문서들을 요약하고 링크해 만듭니다. 내용을 중복해서 관리하지 않습니다.

## AGENTS.md 템플릿

`templates/AGENTS.md`는 매 요청에 들어가는 상시 규칙이라 짧은 영어로 썼습니다.

- 금지 사항
- 슬라이스 루프: 구현 → `check` → 문서 → 커밋
- 문서 규칙, 답변 형식(10줄 이내, 남은 시간 먼저), 마무리 규칙, 스킬 지도

보고와 문서는 과제 언어(기본 한국어)로 쓰도록 지시합니다. Codex는 세션을 시작할 때 AGENTS.md를 읽으니, 고친 뒤에는 `/new`로 새 대화를 시작해야 반영됩니다.

## 제한된 환경에서 쓸 때

환경의 규칙과 과제별 규칙이 이 문서보다 우선합니다.

- 제공된 Codex만 씁니다. 업데이트를 권해도 업데이트하지 않습니다.
- 공개 저장소는 clone할 수 있지만 push, 업로드, 문제·파일·결과물의 외부 전송은 하지 않습니다.
- Computer Use 같은 화면·브라우저 자동 조작, 외부 AI 연결, 환경 통제 우회는 하지 않습니다. 화면 확인은 사람이 미리보기에서 직접 합니다.
- 외부 자료로 결과물을 통째로 대체하지 않습니다. 이 저장소에는 정답 코드가 없습니다.

## 만든 방식

원칙과 실패 유형은 작성자가 정의했고, 스킬 초안은 AI 에이전트로 작성했습니다.

같은 모의 과제를 스킬 없이(기준선), 그리고 스킬을 적용해 실행하고 결과를 비교했습니다. 기준선에서 관찰된 실패는 이렇습니다.

- 검증 없이 한 번에 몰아서 구현
- 커밋 누락
- `127.0.0.1` 바인딩으로 미리보기 불가
- 과제 README와 담당자 답변의 충돌을 조용히 넘기기
- 마감 직전 기능 추가

스킬은 이 실패들을 막도록 고쳤고, 재테스트로 개선을 확인했습니다. 모의 실행도 AI 에이전트로 했으므로, 실제 환경에서는 짧은 리허설을 권합니다.

## 구조와 점검

```text
.agents/skills/<skill>/SKILL.md   스킬 6개 (kickoff/templates.md: 문서 양식)
templates/AGENTS.md               작업 공간용 AGENTS.md 템플릿
install.sh                        설치 스크립트 (파일 복사만)
scripts/validate_skills.py        구조 점검 (의존성 없음)
```

```bash
python3 scripts/validate_skills.py
codex debug prompt-input "hi" | grep -o -E "(kickoff|clarify|checkpoint|audit|wrapup|debrief): Use when" | sort -u   # API 호출 없이 인식 확인
```

# Study Log

## 2026-06-26

### 오늘 한 일
- CloudOps Lab 프로젝트를 시작했다.
- GitHub에 올릴 기본 폴더 구조를 만들었다.
- 이번 방학 목표를 AWS 기반 배포·운영 경험 만들기로 정했다.

### 배운 것
- 프로젝트는 처음부터 완벽하게 만들기보다 기록을 남기며 진행해야 한다.
- 클라우드 엔지니어 준비는 Linux, AWS, GitHub, 배포 경험이 중요하다.

### 내일 할 일
- [x] Git 기본 명령어 정리
- [x] FastAPI 개발환경 세팅
- [x] `/health` API 만들기

## 2026-06-27

### 오늘 한 일 
- CloudOps Lab 프로젝트를 시작했다.
- GitHub 레포와 기본 폴더 구조를 만들었다.
- FastAPI 개발환경을 세팅했다.
- `/health` API를 만들고 로컬 서버에서 실행을 확인했다.
- README 파일명 오타(`REEADME.md`)를 `README.md`로 수정했다.

### 배운 것
- `uvicorn app.main:app --reload`는 `app/main.py` 안에 있는 `app` 객체를 실행한다.
- FastAPI에서 `app = FastAPI()` 객체가 없으면 `Attribute "app" not found` 에러가 발생할 수 있다.
- `.gitignore`에 `venv/`를 넣어야 가상환경 폴더가 GitHub에 올라가지 않는다.
- `git add -A`는 새 파일, 수정 파일, 삭제 파일까지 한 번에 스테이징한다.

### 막힌 것
- 처음 서버 실행 시 `Attribute "app" not found in module "app.main"` 에러가 발생했다.
- README 파일명을 `REEADME.md`로 잘못 만들어 Git에서 삭제/새 파일로 인식했다.

### 해결
- `app/main.py`에 `app = FastAPI()`를 제대로 작성해서 서버 실행 문제를 해결했다.
- `REEADME.md`를 `README.md`로 바꾸고 `git add -A`로 변경사항을 반영했다.

### 내일 할 일
- [ ] Git 기본 명령어 정리하기
- [ ] `/logs` API 만들기
- [ ] README에 로컬 실행 방법 추가하기
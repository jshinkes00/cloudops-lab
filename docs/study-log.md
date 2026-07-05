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

- `/logs` API를 추가했다.
- FastAPI의 `BaseModel`을 사용해서 요청 데이터 형식을 정의했다.
- `/docs`에서 POST 요청과 GET 요청을 테스트했다.
- `GET /logs`와 `POST /logs`의 역할 차이를 확인했다.
- `Address already in use` 에러는 기존 uvicorn 서버가 8000번 포트를 사용 중일 때 발생한다는 것을 알았다.

### 1. `uvicorn app.main:app --reload`에서 각각의 뜻
- `app.main`: app폴더 안에 있는 main.py
- 마지막 `app`: main.py안에 app= fastapi() 변수명
- `--reload`: 코드를 수정하면 서버를 자동으로 다시 실행해주는 옵션

### 2. `GET /logs`와 `POST /logs` 차이
- GET /logs: 현재 저장된 로그 목록을 조회하는 api
- POST /logs:클라이언트가 보낸 데이터를 받아서 새 로그를 생성하는 api

### 3. `logs = []`의 한계
- 서버가 꺼지면: 파이썬의 리스트 자료구조를 사용하여 데이터 임시저장 서버를 끄면 데이터 사라진다
- 그래서 나중에 필요한 것:sql lite 를 사용하여 데이터를 실제로  저장




## 2026-07-01
- 로그 데이터에 `id`를 추가했다.
- `GET /logs/{log_id}` API로 특정 로그 1개를 조회할 수 있게 만들었다.
- `DELETE /logs/{log_id}` API로 특정 로그를 삭제할 수 있게 만들었다.
- `HTTPException`을 사용해서 로그를 찾지 못했을 때 404 에러를 반환하도록 했다.
- 아직 데이터는 `logs = []` 리스트에 저장되므로 서버를 재시작하면 사라진다.

### 오늘 퀴즈 오답 정리

- `POST /logs`는 새 로그를 생성하는 API이다.
- `GET /logs`는 저장된 로그 목록을 조회하는 API이다.
- `logs = []`는 파이썬 리스트이며 메모리에 임시 저장된다.
- 서버를 끄거나 재시작하면 메모리에 있던 데이터는 사라진다.
- 그래서 나중에는 SQLite 같은 데이터베이스가 필요하다.
- `Attribute "app" not found` 에러는 `main.py` 안에 `app = FastAPI()` 객체가 없거나 저장되지 않았을 때 발생할 수 있다.
- `Address already in use`는 8000번 포트를 이미 다른 서버가 사용 중이라는 뜻이다.


## 2026-07-06

### 오늘 한 일
- 기존 `logs = []` 메모리 저장 방식에서 SQLite 저장 방식으로 변경했다.
- `app/database.py` 파일을 만들고 SQLite 연결 함수를 작성했다.
- `POST /logs` 요청이 들어오면 SQLite DB에 로그를 저장하도록 수정했다.
- `GET /logs` 요청이 들어오면 SQLite DB에서 로그 목록을 조회하도록 수정했다.
- 서버를 껐다 켜도 데이터가 유지되는지 확인했다.

### 배운 것
- `logs = []`는 메모리에 저장되기 때문에 서버를 끄면 데이터가 사라진다.
- SQLite는 파일 기반 데이터베이스라서 서버를 재시작해도 데이터가 유지된다.
- `INSERT`는 데이터를 추가할 때 사용한다.
- `SELECT`는 데이터를 조회할 때 사용한다.
- `connection.commit()`을 해야 DB 변경사항이 실제로 저장된다.
- `cursor.fetchall()`은 조회 결과를 여러 개 가져올 때 사용한다.

### 막힌 것
- `get_connection` 함수를 import하지 못하는 에러가 발생했다.

### 해결
- `app/database.py` 안에 `get_connection()`과 `init_db()` 함수를 제대로 작성해서 해결했다.

### 다음 할 일
- [ ] `GET /logs/{log_id}`를 SQLite 방식으로 구현하기
- [ ] `DELETE /logs/{log_id}`를 SQLite 방식으로 구현하기
- [ ] README에 SQLite 사용 내용 추가하기

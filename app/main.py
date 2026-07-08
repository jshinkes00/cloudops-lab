# FastAPI 프레임워크에서 FastAPI 클래스를 가져옴
# FastAPI: API 서버 객체를 만들 때 사용
from fastapi import FastAPI

# Pydantic의 BaseModel을 가져옴
# 클라이언트가 보내는 JSON 데이터 형식을 정의하고 검사할 때 사용
from pydantic import BaseModel

# asynccontextmanager는 FastAPI 앱의 시작/종료 시점에 실행할 코드를 만들 때 사용
# lifespan 방식에서 필요함
from contextlib import asynccontextmanager

# 우리가 만든 database.py에서 DB 관련 함수 가져오기
from app.database import get_connection, init_db


# lifespan 함수
# FastAPI 앱이 시작될 때와 종료될 때 실행할 작업을 정의함
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 앱 시작 시 실행되는 부분
    # 서버가 켜질 때 DB와 logs 테이블을 준비함
    init_db()

    # yield 이전: 서버 시작 시 실행
    # yield 이후: 서버 종료 시 실행
    yield

    # 앱 종료 시 실행되는 부분
    # 지금은 종료할 때 따로 정리할 작업이 없어서 pass
    pass


# FastAPI 앱 객체 생성
# lifespan=lifespan을 넣어서 서버 시작 시 init_db()가 실행되게 함
# uvicorn app.main:app --reload 에서 마지막 app이 바로 이 변수임
app = FastAPI(lifespan=lifespan)


# POST /logs 요청으로 들어올 데이터 형식 정의
# 사용자는 category와 content만 보냄
class LogCreate(BaseModel):
    # 기록 종류: study, workout, weight 등
    category: str

    # 기록 내용
    content: str


# GET /
# API 기본 접속 확인용
@app.get("/")
def root():
    return {"message": "CloudOps Lab API"}


# GET /health
# 서버가 정상 작동 중인지 확인하는 API
@app.get("/health")
def health_check():
    return {"status": "ok"}


# GET /logs
# SQLite DB에 저장된 전체 로그 목록 조회
@app.get("/logs")
def get_logs():
    # DB 연결 생성
    connection = get_connection()

    # SQL 실행용 cursor 생성
    cursor = connection.cursor()

    # logs 테이블에서 모든 로그 조회
    # ORDER BY id DESC는 최신 로그가 위로 오게 정렬한다는 뜻
    cursor.execute("SELECT id, category, content FROM logs ORDER BY id DESC")

    # 조회 결과 전체 가져오기
    rows = cursor.fetchall()

    # DB 연결 닫기
    connection.close()

    # sqlite3.Row 객체를 일반 dict로 변환해서 반환
    logs = []
    for row in rows:
        logs.append({
            "id": row["id"],
            "category": row["category"],
            "content": row["content"]
        })

    return logs


# POST /logs
# 새 로그를 SQLite DB에 저장
@app.post("/logs")
def create_log(log: LogCreate):
    # DB 연결 생성
    connection = get_connection()

    # SQL 실행용 cursor 생성
    cursor = connection.cursor()

    # logs 테이블에 새 데이터 추가
    # ?는 SQL Injection을 막기 위한 자리표시자
    cursor.execute(
        "INSERT INTO logs (category, content) VALUES (?, ?)",
        (log.category, log.content)
    )

    # 방금 생성된 데이터의 id 가져오기
    new_log_id = cursor.lastrowid

    # 변경사항 저장
    connection.commit()

    # DB 연결 닫기
    connection.close()

    # 생성된 로그 정보를 응답으로 반환
    return {
        "message": "log created",
        "log": {
            "id": new_log_id,
            "category": log.category,
            "content": log.content
        }
    }

# GET /logs/{log_id}
# SQLite DB에서 특정 id를 가진 로그 하나만 조회하는 API
@app.get("/logs/{log_id}")
def get_log(log_id: int):
    # DB 연결 생성
    connection = get_connection()

    # SQL 명령어 실행용 cursor 생성
    cursor = connection.cursor()

    # logs 테이블에서 id가 log_id와 같은 데이터 하나 조회
    # ? 자리에는 아래 튜플의 log_id 값이 들어감
    cursor.execute(
        "SELECT id, category, content FROM logs WHERE id = ?",
        (log_id,)
    )

    # 조회 결과 한 줄 가져오기
    # 결과가 있으면 row에 데이터가 들어가고, 없으면 None이 들어감
    row = cursor.fetchone()

    # DB 연결 닫기
    connection.close()

    # 해당 id의 로그가 없으면 404 에러 반환
    if row is None:
        raise HTTPException(status_code=404, detail="Log not found")

    # 조회 결과를 JSON으로 반환
    return {
        "id": row["id"],
        "category": row["category"],
        "content": row["content"]
    }


# DELETE /logs/{log_id}
# SQLite DB에서 특정 id를 가진 로그를 삭제하는 API
@app.delete("/logs/{log_id}")
def delete_log(log_id: int):
    # DB 연결 생성
    connection = get_connection()

    # SQL 명령어 실행용 cursor 생성
    cursor = connection.cursor()

    # 삭제하기 전에 해당 로그가 존재하는지 먼저 조회
    cursor.execute(
        "SELECT id, category, content FROM logs WHERE id = ?",
        (log_id,)
    )

    # 조회 결과 한 줄 가져오기
    row = cursor.fetchone()

    # 삭제할 로그가 없으면 DB 연결 닫고 404 에러 반환
    if row is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Log not found")

    # 해당 id의 로그 삭제
    cursor.execute(
        "DELETE FROM logs WHERE id = ?",
        (log_id,)
    )

    # 삭제 변경사항 저장
    connection.commit()

    # DB 연결 닫기
    connection.close()

    # 삭제한 로그 정보를 응답으로 반환
    return {
        "message": "log deleted",
        "log": {
            "id": row["id"],
            "category": row["category"],
            "content": row["content"]
        }
    }
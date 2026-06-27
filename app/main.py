# FastAPI 프레임워크에서 FastAPI 클래스를 가져옴
# 이걸로 API 서버를 만들 수 있음
from fastapi import FastAPI

# Pydantic의 BaseModel을 가져옴
# 클라이언트가 보내는 JSON 데이터 형식을 정의하고 검증할 때 사용함
from pydantic import BaseModel


# FastAPI 앱 객체 생성
# uvicorn app.main:app --reload 에서 마지막 app이 바로 이 변수임
app = FastAPI()


# 아직 DB를 사용하지 않기 때문에 임시로 리스트에 데이터를 저장함
# 서버를 끄면 이 데이터는 사라짐
logs = []


# POST /logs 요청으로 들어올 데이터 형식 정의
# category와 content는 반드시 문자열이어야 함
class LogCreate(BaseModel):
    # 기록 종류: study, workout, weight 등
    category: str

    # 기록 내용
    content: str


# GET / 요청
# API가 정상적으로 열리는지 확인하는 기본 경로
@app.get("/")
def root():
    return {"message": "CloudOps Lab API"}


# GET /health 요청
# 서버 상태 확인용 API
@app.get("/health")
def health_check():
    return {"status": "ok"}


# GET /logs 요청
# 현재 저장된 기록 목록을 조회함
@app.get("/logs")
def get_logs():
    return logs


# POST /logs 요청
# 클라이언트가 보낸 기록 데이터를 logs 리스트에 추가함
@app.post("/logs")
def create_log(log: LogCreate):
    # 요청으로 들어온 log 데이터를 리스트에 저장
    logs.append(log)

    # 저장 완료 응답 반환
    return {
        "message": "log created",
        "log": log
    }
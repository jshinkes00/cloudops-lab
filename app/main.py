# FastAPI 프레임워크에서 FastAPI 클래스를 가져옴
# FastAPI는 API 서버를 만들 때 사용하는 프레임워크
from fastapi import FastAPI, HTTPException

# Pydantic의 BaseModel을 가져옴
# 클라이언트가 보내는 JSON 데이터의 형식을 정의하고 검사할 때 사용
from pydantic import BaseModel


# FastAPI 앱 객체 생성
# uvicorn app.main:app --reload 에서 마지막 app이 바로 이 변수
app = FastAPI()


# 아직 DB를 사용하지 않기 때문에 임시로 리스트에 데이터를 저장함
# 서버를 끄거나 재시작하면 이 안의 데이터는 사라짐
logs = []


# 로그 id를 만들기 위한 변수
# 새 로그가 생성될 때마다 1씩 증가시킬 예정
next_id = 1


# 클라이언트가 POST /logs로 보낼 데이터 형식
# 사용자가 직접 보내는 값은 category와 content만 있음
class LogCreate(BaseModel):
    # 기록 종류: study, workout, weight 등
    category: str

    # 기록 내용
    content: str


# GET /
# API 서버 기본 접속 확인용
@app.get("/")
def root():
    return {"message": "CloudOps Lab API"}


# GET /health
# 서버 상태 확인용 API
@app.get("/health")
def health_check():
    return {"status": "ok"}


# GET /logs
# 현재 저장된 전체 로그 목록 조회
@app.get("/logs")
def get_logs():
    return logs


# POST /logs
# 새 로그 생성
@app.post("/logs")
def create_log(log: LogCreate):
    # 함수 안에서 전역 변수 next_id 값을 수정하기 위해 global 사용
    global next_id

    # 새 로그 데이터 생성
    # 사용자가 보낸 category/content에 서버가 id를 붙여줌
    new_log = {
        "id": next_id,
        "category": log.category,
        "content": log.content
    }

    # logs 리스트에 새 로그 추가
    logs.append(new_log)

    # 다음 로그를 위해 id 값을 1 증가
    next_id += 1

    # 생성된 로그를 응답으로 반환
    return {
        "message": "log created",
        "log": new_log
    }


# GET /logs/{log_id}
# 특정 id를 가진 로그 1개 조회
@app.get("/logs/{log_id}")
def get_log(log_id: int):
    # logs 리스트에서 id가 log_id와 같은 로그를 찾음
    for log in logs:
        if log["id"] == log_id:
            return log

    # 반복문을 다 돌았는데도 못 찾으면 404 에러 반환
    raise HTTPException(status_code=404, detail="Log not found")


# DELETE /logs/{log_id}
# 특정 id를 가진 로그 삭제
@app.delete("/logs/{log_id}")
def delete_log(log_id: int):
    # enumerate는 인덱스와 값을 같이 꺼내줌
    # index: 리스트에서 몇 번째인지
    # log: 실제 로그 데이터
    for index, log in enumerate(logs):
        if log["id"] == log_id:
            # 해당 위치의 로그를 리스트에서 삭제
            deleted_log = logs.pop(index)

            # 삭제한 로그 정보를 응답으로 반환
            return {
                "message": "log deleted",
                "log": deleted_log
            }

    # 삭제할 id를 찾지 못하면 404 에러 반환
    raise HTTPException(status_code=404, detail="Log not found")
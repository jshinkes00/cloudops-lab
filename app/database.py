# sqlite3는 파이썬에 기본으로 들어있는 SQLite 사용 모듈
# 따로 pip install 안 해도 됨
import sqlite3


# SQLite DB 파일 이름
# 이 파일 안에 로그 데이터가 저장됨
DB_NAME = "cloudops_lab.db"


# DB 연결을 만들어주는 함수
def get_connection():
    # sqlite3.connect()는 SQLite DB 파일에 연결함
    # 파일이 없으면 자동으로 새로 만들어짐
    connection = sqlite3.connect(DB_NAME)

    # row_factory를 설정하면 조회 결과를 딕셔너리처럼 다루기 쉬워짐
    connection.row_factory = sqlite3.Row

    # DB 연결 객체 반환
    return connection


# logs 테이블을 만드는 함수
def init_db():
    # DB 연결 생성
    connection = get_connection()

    # SQL 명령어를 실행하기 위한 cursor 생성
    cursor = connection.cursor()

    # logs 테이블 생성
    # IF NOT EXISTS는 이미 테이블이 있으면 새로 만들지 말라는 뜻
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    # 변경사항 저장
    connection.commit()

    # DB 연결 닫기
    connection.close()
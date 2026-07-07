# SQLite Notes

## 지금 SQLite를 쓰는 이유

처음에는 `logs =[]` 리스트에 데이터를 저장했다.

하지만 이 방식은 서버가 실행 중일 때만 데이터가 유지된다.
서버를 그거나 재시작하면 리스트 안의 데이터는 사라진다.

SQLite는 데이터를 `.db` 파일에 저장한다.
그래서 서버를 껐다 켜도 데이터 유지된다.

---

## SQL 기본 명령어

### INSERT

데이터를 추가할때 사용한다,

```sql
INSERT INTO logs (category, content) VALUES (?, ?);

//데이터를 조회할때 사용한다
SELECT id, category, content FROM logs;

//특정 조건에 맞는 데이터만 조회할 때 사용한다.

SELECT id, category, content FROM logs WHERE id =?;

//특정 조건에 맞는 데이터를 삭제할 때 사용한다.

DELETE FROM logs WHERE id = ?;


WHERE id = ?는 id가 특정 값과 같은 데이터만 찾겠다는 뜻이다.

//예를 들어 사용자가 /logs/3으로 요청하면 서버는 DB에서 id가 3인 로그를 찾는다.

SELECT id, category, content FROM logs WHERE id = 3;

//하지만 코드에서는 직접 3을 문자열에 넣지 않고 ?를 사용한다.

```
## where id = ?는 id가 특정 값과 같은 데이터만 찾겠다는 뜻이다
``` python
cursor.execute(
    "SELECT id, category, content FROM logs WHERE id =?", (log_id,)
)


# CloudOps Lab

클라우드 엔지니어 직무의 시작점을 잡기 위해 진행하는 AWS 기반 서비스 배포·운영 실습 프로젝트입니다.

이번 프로젝트의 목표는 단순한 웹/API 개발이 아니라 Linux 서버 운영, AWS EC2 배포, Docker, CI/CD, 로깅과 트러블슈팅 경험을 GitHub에 기록으로 남기는 것입니다.

## Goals

- Linux 기본 명령어 학습
- FastAPI 기반 간단 API 개발
- AWS EC2 Ubuntu 서버 배포
- Nginx Reverse Proxy 구성
- systemd 서비스 등록
- Docker 기반 실행
- GitHub Actions 기반 배포 자동화 실습
- 로그 확인 및 트러블슈팅 문서화
- AWS CLF-C02 자격증 준비

## Tech Stack

- Python
- FastAPI
- Linux
- AWS EC2
- Nginx
- Docker
- GitHub Actions

## Progress

- [x] 프로젝트 초기 세팅
- [x] FastAPI 로컬 서버 실행
- [x] `/health` API 구현
- [ ] SQLite 연결
- [ ] AWS EC2 배포
- [ ] Nginx 설정
- [ ] systemd 서비스 등록
- [ ] Docker 적용
- [ ] GitHub Actions 배포 자동화
- [ ] CLF-C02 공부 기록 정리

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API 기본 메시지 확인 |
| GET | `/health` | 서버 상태 확인 |
| GET | `/logs` | 기록 목록 조회 |
| POST | `/logs` | 기록 생성 |

## Example Request

```json
{
  "category": "study",
  "content": "FastAPI logs API를 만들었다."
}
```

## Test URL

- Swagger Docs: `http://127.0.0.1:8000/docs`
- Health Check: `http://127.0.0.1:8000/health`
- Logs: `http://127.0.0.1:8000/logs`
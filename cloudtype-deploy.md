# Cloudtype.io 배포 가이드

## 1. GitHub 준비

### 1.1 GitHub 리포지토리 생성
1. GitHub에서 새 리포지토리를 생성합니다
2. 로컬 프로젝트를 GitHub에 업로드합니다:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

## 2. Cloudtype.io 배포

### 2.1 Cloudtype.io 가입 및 설정
1. [cloudtype.io](https://cloudtype.io)에 접속하여 회원가입
2. GitHub 계정으로 로그인

### 2.2 새 프로젝트 생성
1. 대시보드에서 "새 프로젝트" 클릭
2. "GitHub 연동" 선택
3. 배포할 리포지토리 선택
4. 브랜치: `main` 선택

### 2.3 배포 설정
- **빌드 명령어**: (비워둠 - Dockerfile 사용)
- **실행 명령어**: (비워둠 - Dockerfile에서 정의)
- **포트**: 8080
- **환경변수**: 필요시 추가

### 2.4 배포 실행
1. "배포하기" 클릭
2. 빌드 로그 확인
3. 배포 완료 후 제공되는 URL로 접속

## 3. 주요 파일 설명

### 3.1 Dockerfile
- Python 3.11 베이스 이미지 사용
- 의존성 설치 및 애플리케이션 실행 설정
- 포트 8080 노출

### 3.2 requirements.txt
- Python 패키지 의존성 정의
- pyproject.toml에서 추출한 주요 패키지들

### 3.3 .dockerignore
- Docker 빌드 시 제외할 파일들 정의
- 불필요한 파일들을 제외하여 빌드 속도 향상

## 4. 배포 후 확인사항

### 4.1 기능 테스트
- 홈페이지 접속 확인
- 각 메뉴 (서비스 소개, 통계, 뉴스, 판례, 관련기관·법률) 동작 확인
- 데이터 로딩 확인 (CSV, Excel 파일)

### 4.2 문제 해결
- 로그 확인: Cloudtype 대시보드에서 로그 확인
- 환경변수 설정: 필요시 환경변수 추가
- 재배포: 코드 수정 후 GitHub push로 자동 재배포

## 5. 자동 배포 설정

GitHub에 코드를 push하면 자동으로 재배포됩니다:

```bash
git add .
git commit -m "Update message"
git push origin main
```

## 6. 도메인 설정 (선택사항)

Cloudtype.io에서 제공하는 기본 도메인 외에 커스텀 도메인을 설정할 수 있습니다:
1. 도메인 설정 메뉴에서 원하는 도메인 추가
2. DNS 설정에서 CNAME 레코드 추가
3. SSL 인증서 자동 적용

## 7. 모니터링

- 애플리케이션 상태 모니터링
- 리소스 사용량 확인
- 로그 실시간 모니터링 
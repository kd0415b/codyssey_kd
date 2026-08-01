codyssey_kd

## 트러블슈팅

### 오류 1: hello.py Not Found
**원인:** hello.py를 이미지 빌드 이후에 생성해서 이미지 안에 포함되지 않음

**해결 과정:**
1. Dockerfile에 COPY 명령어 확인
2. hello.py 생성 후 이미지 재빌드: docker build -t codyssey .
3. 재빌드한 이미지로 실행: docker run codyssey python hello.py
4. 정상 실행 확인

# 깃허브 연결하기
```
# 1. Git 초기화 (새로운 저장소 만들 때)
git init

# 2. 원격 저장소 연결 (GitHub 저장소 주소 추가)
git remote add origin https://github.com/사용자이름/저장소이름.git

# 3. 변경된 파일 추가 (전체 추가)
git add .

# 4. 커밋 (변경 사항 저장)
git commit -m "커밋 메시지"

# 5. 원격 저장소로 푸시 (GitHub에 업로드)
git push https://<토큰>@github.com/LeebaeS/stock.git main
```
## 토큰 만드는 방법
1. https://github.com/settings/tokens 페이지에서 Generate new token (classic) 클릭
2. repo 체크
3. 맨 아래 Generate Token 클릭
4. ⭐⭐⭐ 생성된 토큰 반드시 복사 해야 함. 한번 나가면 다시 못 봄 ⭐⭐⭐


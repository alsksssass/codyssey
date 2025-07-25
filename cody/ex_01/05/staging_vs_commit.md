
# Git - 스테이징과 커밋의 차이 (간단 정리)

## ✅ 스테이징 (git add)

- **역할**: 커밋할 변경 파일을 선택해 임시 저장하는 단계
- **명령어**: `git add 파일명`
- **예시**:
  ```bash
  git add main.py
````

## ✅ 커밋 (git commit)

* **역할**: 스테이징된 파일들을 하나의 버전으로 저장
* **명령어**: `git commit -m "설명"`
* **예시**:

  ```bash
  git commit -m "기능 추가"
  ```

## ⚖️ 차이 비교

| 구분    | 스테이징 (git add)  | 커밋 (git commit) |
| ----- | --------------- | --------------- |
| 목적    | 커밋할 파일 선택       | 선택된 파일을 기록      |
| 기록 여부 | Git에 아직 기록되지 않음 | Git 히스토리에 기록됨   |
| 수정 가능 | 다시 add로 변경 가능   | 커밋 후에는 reset 필요 |

## 📌 전체 흐름

```bash
# 1. 파일 수정
vim app.py

# 2. 스테이징
git add app.py

# 3. 커밋
git commit -m "메시지"
```


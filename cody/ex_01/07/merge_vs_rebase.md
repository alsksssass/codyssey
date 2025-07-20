
````markdown
# 🔀 Git Merge vs Rebase: 차이점과 협업 시 Merge 추천 이유

---

## 📌 개념 요약

| 구분 | `git merge` | `git rebase` |
|------|-------------|---------------|
| 목적 | **브랜치의 변경 사항을 통합** | **커밋 이력을 한 줄로 정리** |
| 커밋 이력 | **브랜치가 병합된 흔적**이 남음 | **이력이 깔끔하게 정리**됨 (선형화) |
| 사용 예시 | 기능 브랜치를 main에 통합할 때 | 작업 중 최신 이력으로 브랜치 정리할 때 |
| 충돌 처리 | 병합 시점 1회 발생 | 커밋마다 충돌 발생 가능 |
| 원격 브랜치 | 영향 없음 | **주의 필요** – 이미 푸시된 커밋을 rebase하면 위험함 |

---

## 🔧 예시 시각화

```bash
# 상황: feature 브랜치를 main에 반영하고 싶을 때
````

### 🔷 Merge 사용 시 이력

```
*   e4f Merge branch 'feature'
|\
| * d3f 작업 A
| * c2e 작업 B
* | a1b 기존 커밋
|/
```

### 🔶 Rebase 사용 시 이력

```
* d3f 작업 A (rebased)
* c2e 작업 B (rebased)
* a1b 기존 커밋
```

---

## 💡 협업 시 `merge`를 추천하는 이유

1. ### 🔍 **이력 추적이 명확하다**

   * 누가, 언제, 어떤 브랜치를 병합했는지 확인 가능
   * 팀 작업 흐름 이해에 유리

2. ### 💥 **리베이스는 충돌 가능성이 높고 위험하다**

   * 이미 push한 브랜치를 rebase하면 히스토리 충돌 발생
   * 협업 중인 브랜치에서 rebase 후 강제 푸시는 **데이터 손실 위험**

3. ### 🔄 **작업 이력 공유가 자연스럽다**

   * merge는 브랜치 흐름을 보존하기 때문에 **코드 리뷰**나 **디버깅**에 유리

4. ### 🚫 **강제 푸시가 필요 없다**

   * merge는 일반 푸시로도 충분
   * 반면 rebase는 `git push --force` 필요 → 다른 사람 작업을 덮어쓸 수 있음

---

## ✅ 결론

> **혼자 작업할 때는 `rebase`로 이력을 깔끔하게 정리하고,**
>
> **협업 중에는 `merge`로 안정성과 이력 추적성을 확보하자.**

---

## 📎 참고 명령어

```bash
# merge 방식
git checkout main
git merge feature
git push origin main

# rebase 방식 (주의!)
git checkout feature
git rebase main
git push --force-with-lease
```

---

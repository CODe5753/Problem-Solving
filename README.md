# 다시보기
### 11729
### 1652
### 1032 : 계속 런타임에러 뜸
### 1991 자료구조 노드 연습중 - 수정필요
### 5522 : 런타임 에러

# 주의사항
### Python 런타임에러 : 입력시 .split()으로 나눠 받기
### input() 보다 sys.stdin.readline 사용하는게 속도가 훨씬 빠르다!!!!!!!!!!!
### 단, readline 하면 개행문자도 함께 저장되니까 문자열만 저장할 때는 rstrip()을 쓰자!..

### [PyPy3]2751 : 수 정렬하기2 REVIEW
알고리즘은 정상 작동했으나 Python 자체 속도의 문제로 반복되는 [시간초과]...
sys.stdin.readline을 사용해봤으나 readline의 개행문자가 같이 들어가서 오류가 떴고
.rstrip()으로 겨우 해결했다
소스 제출은 PyPy3로 성공!
시간복잡도를 떠나서 파이썬 내장 sorted로 해결 되는걸 보니 입출력의 시간문제였다..
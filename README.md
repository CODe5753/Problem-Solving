# TRYING
11729 : 하노이 탑 이동 순서 [분할정복]
1991 : 트리순회 자료구조 [트리] 노드 연습중 - 수정필요  
6064 : 카잉달력  
1913 : 달팽이  
1699 : 제곱수의 합 dp[i-j**2]+1 이해  
1303 : 전쟁-전투 마저하기  
1654 : 랜선 - 이분탐색 알고리즘 이해하기  
1018 : 체스판 다시 칠하기 - 조건문 노가다  
5463 : 건포도 - 아마 DFS  
1509 : palindrome
13545 : 모스알고리즘
13547 : 모스알고리즘
# CAREFUL
* Python 런타임에러 : 입력시 .split()으로 나눠 받기
* input() 보다 sys.stdin.readline 사용하는게 속도가 훨씬 빠르다!!!!!!!!!!!
* 단, readline 하면 개행문자도 함께 저장되니까 문자열만 저장할 때는 rstrip()을 쓰자!..
* 입력시 N,K=map(int,input().split())
* 10867中 print('CY' if int(input()) % 2 else 'SK')처럼 print내에 조건문 가능
* 한 변수에 값 반복문으로 한줄 작성 : t=list([int(input()) for _ in range(5)])
* l,a,b,c,d= (int(input()) for _ in range(5)) 이것도된다
# REVIEW
### 1920 수 찾기
이분탐색 문제다 binarysearch 함수를 만들고 돌리는 문제.  
계속 시간초과 뜨길래 첫번째로 input()을 sys.stdin.readline으로 바꾸고 python3으로 제출했고  
또 시간초과 뜨길래 pypy3로 제출하니까 통과했다.. 아마 입력 갯수가 10만개라 그런지 input()은 느렸나보다.
### 1652 누울 자리를 찾아라
머리가 돌아가질 않았다.. 안보고 겨우 두 세시간만에 풀었다..
### 2108 통계학
statistics 활용하여 산술평균, 최빈값, 중앙값 등 => 런타임에러떠서 수작업함
### 9012 괄호
소스 포스팅하기
### 2751 수 정렬하기2
알고리즘은 정상 작동했으나 Python 자체 속도의 문제로 반복되는 [시간초과]...  
sys.stdin.readline을 사용해봤으나 readline의 개행문자가 같이 들어가서 오류가 떴고  
.rstrip()으로 겨우 해결했다  
소스 제출은 PyPy3로 성공!  
시간복잡도를 떠나서 파이썬 내장 sorted로 해결 되는걸 보니 입출력의 시간문제였다..

### 1032 명령프롬프트
어려운 문제는 아니다.  
좀 더 간결하게 코딩할 수 있을것 같아서 검색을하다가  
단 세 줄로 이뤄진 코드를 봤다...  
해석은 1032.py에 있다.

### 1094 막대기
일반적인 접근이 아닌 2진법으로 생각했을 때의 풀이를 추가함.

### 10814 나이순 정렬
for i in sorted(data, key=lambda age:age[0]):
list에 두가지 항목이 있지만 한가지 항목을 기준으로만 정렬이 가능함.
만약에 그냥 sorted를 해버리면 두 항목 모두 정렬이 되어버림(숫자별정렬, 문자별정렬)
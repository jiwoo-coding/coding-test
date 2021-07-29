'''
제목 : N과 M(2)

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

'''

import sys
from itertools import combinations  # 조합 표기 방식 이용
input=sys.stdin.readline

n, m = map(int, input().split()) # m=행, n=열

data=[]
for i in range(1, n+1):
    data.append(i)

for lst in combinations(data,m):
    for i in lst:
        print(i, end=' ')
    print()

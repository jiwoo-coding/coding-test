'''
제목 : N과 M(11)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.

'''

import sys
from itertools import product  # 순열 표기 방식 이용
input=sys.stdin.readline

n, m = map(int, input().split()) # m=행, n=열
data=sorted(list(map(int, input().split()))) # 오름차순 정렬, 정수 변환
data=product(data, repeat=m)

for lst in sorted(set(data)):  # 오름차순 정렬, set으로 중복 제거
    print(*lst)  # 참조자를 넣어서 list 형태를 띄어쓰기 단위로 넣을 수 있다.

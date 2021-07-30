'''
제목 : N과 M(9)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.

'''

import sys
from itertools import permutations  # 순열 표기 방식 이용
input=sys.stdin.readline

n, m = map(int, input().split()) # m=행, n=열
data=list(map(int, input().split())) # 정수 변환
data=permutations(data, m)

for lst in sorted(set(data)):  # 오름차순 정렬, set으로 중복 제거
    print(*lst)  # 참조자를 넣어서 list 형태를 띄어쓰기 단위로 넣을 수 있다.

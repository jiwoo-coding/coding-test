'''
**1로 만들기

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.
'''

import sys
input = sys.stdin.readline

def go(x):
    if d[x] >0:  return d[x]
    if x==1:  return 0
    d[x]=go(x-1)+1
    print(x, d)
    if x%3==0:
        k=go(x//3)+1
        if d[x]>k:
            d[x]=k
    if x%2==0:
        k=go(x//2)+1
        if d[x]>k:
            d[x]=k
    print(x, d[x])
    return d[x]

if __name__=="__main__":
    n=int(input())
    d=[-1 for i in range(n+1)]
    print(d)
    print(go(n))
    

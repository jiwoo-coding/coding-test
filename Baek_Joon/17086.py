'''
*아기상어2*
N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

안전 거리가 가장 큰 칸을 구해보자. 
'''

import sys
input = sys.stdin.readline

m,n = map(int, input().split())
data={}
key=[]
num=0
for i in range(m):
    temp=(list(map(int, input().split())))
    for j in range(len(temp)):
        if temp[j]==1:
            key.append((i,j))
        data[num]=(i,j)
        num+=1

result=[]
for x,y in data.values():
    temp=[]
    for t_x, t_y in key:
        if t_x==x or t_y==y:
            dist=abs(t_x-x)+abs(t_y-y)
            temp.append(dist)
        else:
            dist_x=abs(t_x-x)
            dist_y=abs(t_y-y)
            if dist_x>dist_y:
                temp.append(dist_x)
            else:
                temp.append(dist_y)
    result.append(min(temp))
print(max(result))

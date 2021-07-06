'''
*토마토2
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.



창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''

import sys
from collections import deque

n, m, h = map(int, sys.stdin.readline().split()) # m=행, n=열, h=높이
data=[]
start=[]
for i in range(h):
    data.append([])
    for j in range(m):
        data[i].append(list(map(int, sys.stdin.readline().split())))

for i in range(h):
    for j in range(m):
        for k in range(n):
            if data[i][j][k]==1:
                start.append((i,j,k))

deq=deque()
check=[[[0]*(n) for _ in range(m)] for __ in range(h)]

dx=[1,-1,0,0,0,0] 
dy=[0,0,-1,1,0,0]
dh=[0,0,0,0,1,-1]

for s_z, s_x, s_y in start:
    deq.append((s_z, s_x, s_y))

cnt=0
while deq:
    sz, sx, sy=deq.popleft()
    for i in range(6):
        nx=sx+dx[i]
        ny=sy+dy[i]
        nh=sz+dh[i]
        if nx>=0 and nx<m and ny>=0 and ny<n and nh>=0 and nh<h:
            if data[nh][nx][ny]==0 :
                check[nh][nx][ny]=check[sz][sx][sy]+1
                deq.append((nh,nx,ny))
                data[nh][nx][ny]=1

for j in range(h):
    for i in range(m):
        if 0 in data[j][i]:
            cnt=-1
            break

        if cnt<max(check[j][i]):
            cnt=max(check[j][i])
    if cnt==-1:
        break
    
print(cnt)

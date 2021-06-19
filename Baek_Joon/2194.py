'''
* 유닛 이동시키기
스타크래프트와 같은 게임을 하다 보면 어떤 유닛을 목적지까지 이동시켜야 하는 경우가 종종 발생한다. 편의상 맵을 N×M 크기의 2차원 행렬로 생각하자. 또한 각각의 유닛은 크기를 가질 수 있는데, 이를 A×B 크기의 2차원 행렬로 생각하자. 아래는 5×5 크기의 맵과 2×2 크기의 유닛에 대한 한 예이다. S는 시작점을 나타내며 E는 끝점을 나타낸다.



유닛은 상하좌우의 네 방향으로만 움직일 수 있다. 단, 유닛의 일부분이 장애물이 설치된 부분(위의 예에서 색이 칠해진 부분)을 지날 경우, 위의 예에서는 시작 위치에서 위로 이동하는 경우는 허용되지 않는다. 위의 예는 유닛을 오른쪽으로 세 칸, 위쪽으로 세 칸 움직이면 목적지에 도달할 수 있고, 이 경우가 가장 적은 이동 회수를 거치는 경우이다. 이동하는 도중에 유닛이 맵 밖으로 나가는 경우는 허용되지 않는다.

맵의 정보와 유닛의 정보가 주어졌을 때, 유닛을 목적지까지 움직이기 위해 필요한 최소의 이동 회수를 구하는 프로그램을 작성하시오.

'''
import sys
from collections import deque

def move_check(db_map, s_x, s_y, u_m, u_n, key): # key: (up=1, down=2, left=3, right=4)
    ans=True
    
    if key==1 or key==2:
        for u_y in range(s_y, s_y+u_n):  
            if db_map[s_x-1][u_y]==1 and key==1:
                ans=False
            elif db_map[s_x+u_m][u_y]==1 and key==2:
                ans=False
    else:
        for u_x in range(s_x, s_x+u_m):
            if db_map[u_x][s_y-1]==1 and key==3:
                ans=False
            elif db_map[u_x][s_y+u_n]==1 and key==4:
                ans=False
                
    return ans

m, n, u_m, u_n, k  = map(int, sys.stdin.readline().split())
beok=[]
for i in range(k):
    beok.append((list(map(int, sys.stdin.readline().split()))))
s_x, s_y = map(int, sys.stdin.readline().split())
g_x, g_y = map(int, sys.stdin.readline().split())
deq=deque()

# map setting and unit settings
db_map=[[0]*(n+2) for _ in range(m+2)]
check=[[0]*(n+2) for _ in range(m+2)]  # 최단거리 계산용
for i in range(m+2):
    for j in range(n+2):
        if i==0 or i==m+1 or j==0 or j==n+1:
            db_map[i][j]=1   # 외부 벽은 1로 처리
    
# 장애물 settings
for x,y in beok:
    db_map[x][y]=1

tree_cnt=0
deq.append((s_x, s_y))
checking=0

while True:  
    
    s_x, s_y=deq.popleft()
    db_map[s_x][s_y]=1
    if move_check(db_map, s_x, s_y, u_m, u_n, 1): # up
        if db_map[s_x-1][s_y]!=1 and ((s_x-1,s_y) not in deq):
            deq.append((s_x-1,s_y))
            check[s_x-1][s_y]=check[s_x][s_y]+1
    if move_check(db_map, s_x, s_y, u_m, u_n, 2): # down
        if db_map[s_x+1][s_y]!=1 and ((s_x+1,s_y) not in deq):
            deq.append((s_x+1,s_y))
            check[s_x+1][s_y]=check[s_x][s_y]+1
    if move_check(db_map, s_x, s_y, u_m, u_n, 3): # left
        if db_map[s_x][s_y-1]!=1 and ((s_x,s_y-1) not in deq):
            deq.append((s_x,s_y-1))
            check[s_x][s_y-1]=check[s_x][s_y]+1
    if move_check(db_map, s_x, s_y, u_m, u_n, 4): # right
        if db_map[s_x][s_y+1]!=1 and ((s_x,s_y+1) not in deq):
            deq.append((s_x,s_y+1))
            check[s_x][s_y+1]=check[s_x][s_y]+1

    if s_x==g_x and s_y==g_y:
        checking=1
        break
    
    if len(deq)==0:
        break
    
if checking==0:
    print(-1)
else:
    print(check[g_x][g_y])

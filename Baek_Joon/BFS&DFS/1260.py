'''
* DFS와 BFS
  그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
  단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
  정점 번호는 1번부터 N번까지이다.
'''


from collections import deque
import sys

def dfs(graph, start, visited):
    visited[start]=True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i,visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            #print('\n start: ',i)
            if not visited[i]:
                queue.append(i)
                visited[i]=True
        

N,M,V = map(int, sys.stdin.readline().split())
temp=[]
for i in range(M):
    temp.append(list(map(int,sys.stdin.readline().split())))
    
graph=[[] for _ in range(N+1)]
for lst in temp:  # tree 형식으로 만들기
    if len(lst)!=0:
        graph[lst[0]].append(lst[1])
        graph[lst[1]].append(lst[0])
for i in range(len(graph)): # 정렬
    graph[i].sort()

visited=[False]*(N+1) 
dfs(graph, V, visited)
print()
visited=[False]*(N+1)
bfs(graph, V, visited)

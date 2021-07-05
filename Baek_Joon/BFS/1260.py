from collections import deque

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
        

N,M,V = map(int, input().split())
temp=[]
for i in range(M):
    temp.append(list(map(int,input().split())))
    
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

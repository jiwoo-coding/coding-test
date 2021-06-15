from collections import deque

num=int(input())
a, b=map(int, input().split())
m=int(input())
relation=[[] for i in range(n+1)]
ch = [0]*(n+1)
q=deque()

for i in range(m):
  x,y=map(int, input().split())
  relation[x].append(y)
  relation[y].append(x)
  
 q.append(a)

while q:
  n=q.pop(0)
  for i in relation[n]:
    if i != a and ch[i]==0:
      ch[i]=ch[n]+1
      q.append(i)
if ch[b]==0:
  print(-1)
else:
  print(ch[b])

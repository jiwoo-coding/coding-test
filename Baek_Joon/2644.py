***
-촌수계산

우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.
***

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
  n=q.popleft()
  for i in relation[n]:
    if i != a and ch[i]==0:
      ch[i]=ch[n]+1
      q.append(i)
if ch[b]==0:
  print(-1)
else:
  print(ch[b])

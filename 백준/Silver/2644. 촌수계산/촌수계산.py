from collections import deque

#입력 및 그래프 받기
n=int(input())
a,b=map(int,input().split())
line_n=int(input())
graph=[[] for x in range(n+1)]
for i in range(line_n):
    c,d= map(int,input().split())
    graph[c].append(d)
    graph[d].append(c)

#방문정보
visited= [False]*(n+1)

def bfs (start,end):
    j=0
    count=0
    #덱에 넣기
    queue=deque([start])
    #방문처리
    visited[start]=0
    #큐가 빌 때까지 계속
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                #최근 visit은 그 이전 visit보다 1을 더한 값을 준다. 
                visited[i]=visited[v]+1
    if visited[end]==False:
        return -1
    else: 
        #목적한 end의 visited값을 반환하면 된다.
        return visited[end]

print(bfs(a,b))

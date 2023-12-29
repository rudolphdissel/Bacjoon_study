from collections import deque

#입력받기
N,M,V = map(int,input().split())
graph=[[] for _ in range(N+1)]

#그래프 생성
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#그래프 정렬
for i in graph:
    i.sort()


#dfs 함수
def dfs(graph,visited,V):
    #방문처리
    visited[V]=True
    print(V,end=" ")
    #인접한 노드 오름차순으로 탐색
    for i in graph[V]:
        if not visited[i]:
            dfs(graph,visited,i)

#bfs 함수
def bfs(graph,visited,start):
    #큐 구현을 위한 덱 생성
    queue=deque([start])
    visited[start]=True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 원소를 하나 뽑아 출력하기
        x=queue.popleft()
        print(x, end=" ")
        #아직 방문하지 않은 인접한 원소 큐에 삽입
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

#dfs 함수호출
visited=[False]*(N+1)
dfs(graph,visited,V)

#bfs 함수호출
visited=[False]*(N+1)
print()
bfs(graph,visited,V)
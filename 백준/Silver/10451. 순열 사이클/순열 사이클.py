#함수 정의
def dfs(graph,v,visited):
    visited[v]+=1
    if graph[v]==v:
        return 1
    elif visited[v]<=1:
        if visited[graph[v]]==0:
            dfs(graph,graph[v],visited)
            return 1
    else: 
        return 0

    
#입력받기
T=int(input())
for i in range(T):
    a=0
    N=int(input())
    graph=list(map(int,input().split()))
    graph1=[0]
    #그래프 정돈
    for j in graph:
        graph1.append(j)
    #방문기록 초기화
    visited=[0]*(N+1)
    #함수 실행,정답 출력
    for k in range(1,N+1):
        a+=dfs(graph1,k,visited)
    print(a)
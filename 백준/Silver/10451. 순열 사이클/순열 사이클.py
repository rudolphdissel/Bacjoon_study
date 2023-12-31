#함수 정의
def dfs(v):
    visited[v]=True
    next=graph[v]
    if not visited[next]:
        dfs(next)

    
#입력받기
for _ in range(int(input())):
    result=0
    N=int(input())
    graph=[0]+list(map(int,input().split()))
    #방문기록 초기화
    visited=[False]*(N+1)
    #함수 실행,정답 출력
    for k in range(1,N+1):
        if not visited[k]:
            dfs(k)
            result+=1
    print(result)
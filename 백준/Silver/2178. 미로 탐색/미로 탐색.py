#2178번 미로탐색
from collections import deque

#최단경로 찾기 함수
def bfs(x,y):
    #x,y값을 담을 큐 자료구조 생성
    queue=deque()
    queue.append((x,y))
    #큐가 빌 때까지 실행
    while queue:
        x,y=queue.popleft() #큐에서 원소빼서 x,y에 다시 언패킹
        for i in range(4): #상, 하, 좌, 우로 이동하며 확인
            nx=x+dx[i]
            ny=y+dy[i]
            #범위 벗어나면 무시
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            #이동한 곳이 벽이면 무시
            if graph[nx][ny]==0:
                continue
            #왔던 곳 방문표시 + 이동거리 계산
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[N-1][M-1]

#입력받기
graph=[]
N,M=map(int,input().split())
for i in range(N):
    graph.append(list(map(int,input())))

#방향벡터 정의
dx=[1,-1,0,0]
dy=[0,0,1,-1]



#답
print(bfs(0,0))

#이게 너비 우선 탐색이다. 먼저 들어온게 먼저 나가니까, 이 문제의 경우 가장 적은 숫자에서 나올 수 있는 분기부터 
#순차적으로 처리될 수 밖에 없다. 그렇기 때문에 이렇게 넘버링이 되면, 그게 무조건 최소경로다.
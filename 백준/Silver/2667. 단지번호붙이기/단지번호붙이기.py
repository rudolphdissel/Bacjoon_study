#2667 단지번호 붙이기

#너비 우선탐색
from collections import deque

#입력 받기
N=int(input())
graph=[]
for i in range(N):
    graph.append(list(map(int,input())))

#방문정보 구현
visited=[[False]*N for x in range(N)]


#방향벡터 정의
dx=[1,-1,0,0]
dy=[0,0,1,-1]

#함수정의
def bfs(x,y):
    point=1
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        visited[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny]=True
                point+=1
    return point

point_list=[]
quantity=0

#실행
for i in range(N):
    for j in range(N):
        if graph[i][j]==0:
             continue
        if graph[i][j]==1 and not visited[i][j]:
            quantity+=1
            point=bfs(i,j)
            point_list.append(point)
point_list.sort()
print(quantity)
for i in point_list:
    print(i)
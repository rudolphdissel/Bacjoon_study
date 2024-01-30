import sys
board=[['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
n, m = map(int, sys.stdin.readline().split())
ans=n*m

user = []
for _ in range(n):
    user.append(list(sys.stdin.readline().strip('\n')))

def some(x, y):
    cnt=0
    for i in range(8):
        for j in range(8):
            if board[i][j]==user[x+i][y+j]:
                cnt+=1
    return min(cnt, 64-cnt)

for i in range(n-7):
    for j in range(m-7):
        ans=min(ans, some(i, j))
print(ans)
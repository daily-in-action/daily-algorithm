# BOJ-1926 그림
from collections import deque

n, m = map(int, input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0] # 시계방향 선언

picture_count = 0 # 그림이 몇개인가 셈
max_picture = 0 # 그림들 중 제일 큰 그림

data = []
for _ in range(n):
    data += [list(map(int, input().split()))]

check = [] # 방문했었는지 체크하려고 만들어논 0으로 된 리스트
for _ in range(n):
    check += [[0]*m]

def BFS(x,y):
    picture = 1 # 그림의 초기 넓이 값
    queue = deque() # 큐 생성
    queue.append((x,y)) # 초기 값 넣어줌

    while queue: # queue가 빌 때까지
        x, y = queue.popleft() # 시작하는 지점의 값을 받아오고

        for i in range(4): # 그 점의 상하좌우를 탐색할거임
            ax, ay = x+dx[i], y+dy[i] # ax와 ay에 각각 넣어준다(시작점기준 상하좌우값)

            if (ax>=0 and ax<n) and (ay>=0 and ay<m):
                if data[ax][ay] == 1 and check[ax][ay] == 0: # [ax][ay]가 1이고, 방문하지 않았다면
                    queue.append((ax,ay)) # 큐에 넣어줌
                    check[ax][ay] = 1 # 방문했으니 1로 바꿔줌
                    picture += 1
    return picture

for i in range(n):
    for j in range(m):
        if data[i][j] == 1 and check[i][j] == 0:
            picture_count += 1
            check[i][j] = 1 # 방문했으니 1 넣어줌
            max_picture = max(max_picture,BFS(i,j))

print(picture_count)
print(max_picture)
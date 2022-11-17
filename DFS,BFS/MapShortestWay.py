# Problem Reference: [Programmers school] https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 2022.11.18

from collections import deque

def bfs_maze(maps):
    n = len(maps)
    m = len(maps[0])
    ways = [[-1 for i in range(m)] for j in range(n)]
    ways[0][0] = 1

    curX = 0
    curY = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque([(curX, curY)])
    while queue:
        curX, curY = queue.popleft()
        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if nextX < 0 or nextX > n-1 or nextY < 0 or nextY > m-1:
                continue
            if maps[nextX][nextY] == 0:  # 0=벽
                continue
            if ways[nextX][nextY] == -1:
                ways[nextX][nextY] = ways[curX][curY] + 1
                queue.append((nextX, nextY))

    for i in range(n):
        print(ways[i])

    return ways[n - 1][m - 1]


def solution(maps):
    answer = bfs_maze(maps)

    return answer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    solution(arr)

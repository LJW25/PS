# Problem Reference: [Programmers school] https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 2022.11.18

from collections import deque

def solution(n, computers):
    answer = 0

    arr = [0 for i in range(n)]

    def bfs(cur):
        queue = deque([cur])

        while queue:
            cur = queue.popleft()
            arr[cur] = 1
            curConnects = computers[cur]
            for i in range(n):
                if curConnects[i]==1 and i != cur and arr[i] == 0:
                    queue.append(i)
                    arr[i] = 1

    while(sum(arr) < n):
        print(sum(arr))
        print(arr)
        cur = arr.index(0)
        bfs(cur)
        answer+=1


    return answer


def main():
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    answer = solution(n, computers)
    print(f"answer: {answer}")

main()

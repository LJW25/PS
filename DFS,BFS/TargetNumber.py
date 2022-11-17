# Problem Reference: [Programmers school] https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 2022.11.18

def solution(numbers, target):
    answer = [0]
    length = len(numbers)

    def dfs(idx, curSum):
        if idx == length:
            if curSum == target:
                answer[0] += 1
                return 0
        else:
            dfs(idx+1, curSum+numbers[idx])
            dfs(idx+1, curSum-numbers[idx])

    dfs(0,0)
    return answer[0]

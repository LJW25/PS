# Problem Reference: [Programmers school] https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 2022.11.19

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        curPhone = phone_book[i]
        temp = phone_book[i + 1]

        if len(temp) > len(curPhone) and temp[:len(curPhone)] == curPhone:
            return False

    return True
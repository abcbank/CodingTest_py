def collatz(num: int, iteral: int):
    if num == 1:
        return 0
    elif num % 2 == 0:
        num = int(num / 2)
    else:
        num = int(num * 3 + 1)
    if num == 1:
        return iteral + 1
    elif iteral == 499:
        return -1
    else:
        return collatz(num, iteral + 1)

def solution(num):
    answer = collatz(num, 0)
    print(answer)
    return answer
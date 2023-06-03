# 재귀 대신 while 활용
def collatz(num):
    answer = 0
    while num!=1:
        if num%2==0:
            num=num/2
        else:
            num=3*num+1
        answer=answer+1

        if answer>=500:
            return -1

    return answer
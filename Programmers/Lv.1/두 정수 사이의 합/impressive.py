def solution(a, b):    
    # 복잡도를 고려했을 경우의 정답
    # max(a,b) => 찾는데 시간 소요
    # min(a,b) => 찾는데 시간 소요
    # sum => 범위에 따라 시간 소요
    return (abs(a-b)+1)*(a+b)//2
def solution(x):
    return x % sum(int(c) for c in list(str(x))) == 0
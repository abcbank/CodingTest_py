def solution(arr, divisor):
    targets = sorted(list(filter(lambda x: x % divisor == 0, arr)))
    
    if len(targets) > 0:
        return targets
    else:
        return [-1]
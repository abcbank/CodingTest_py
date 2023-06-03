def solution(arr, divisor): 
    # 딱 생각했던 풀이법....!
    # or: 앞의 항이 거짓일 경우 뒤의 항을 출력
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
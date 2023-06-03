def solution(s):
    p_count = 0
    y_count = 0

    for i in s.upper():
        if i == 'P':
            p_count += 1
        elif i == 'S':
            y_count += 1

    return p_count == y_count
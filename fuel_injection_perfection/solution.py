def solution(n):
    if (isinstance(n, str)):
        return solution(int(n))
    if (n == 1):
        return 0
    if (n == 2):
        return 1
    if (n == 3):
        return 2
    if (n & 3 == 0):
        return 2 + solution(n >> 2)
    if (n & 3 == 1):
        return 1 + solution(n - 1)
    if (n & 3 == 2):
        return 1 + solution(n >> 1)
    else:
        return 3 + solution((n + 1) >> 2)

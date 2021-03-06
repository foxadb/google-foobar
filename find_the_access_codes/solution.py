def solution(l):
    if (len(l) < 3):
        return 0
    triple_count = 0
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            for k in range(j + 1, len(l)):
                if ((l[j] % l[i] == 0) and (l[k] % l[j] == 0)):
                    triple_count += 1
    return triple_count


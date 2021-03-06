def get_divisors(l, i):
    # assuming the list is already sorted in ascending order
    return [j for j in range(i) if (l[i] % l[j] == 0)]


def solution(l):
    divisors = {i: get_divisors(l, i) for i in range(len(l))}
    return sum(sum(len(divisors[j]) for j in divisors[i]) for i in divisors.keys())

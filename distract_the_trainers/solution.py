def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def is_not_power_two(n):
    return n & (n - 1) != 0


def is_loop(a, b):
    reduced_sum = (a + b) // gcd(a, b)
    return is_not_power_two(reduced_sum)


def remove_matched_index(trainers, index):
    for i in range(len(trainers)):
        trainers[i] = [x for x in trainers[i] if x != index]
    trainers[index] = [None]


def solution(banana_list):
    n = len(banana_list)
    matching_trainers = [[j for j in range(n) if i != j and is_loop(
        banana_list[i], banana_list[j])] for i in range(n)]
    alone_trainers = 0
    processed_trainer_count = 0
    while (processed_trainer_count < n):
        less_matching_trainer = 0
        for i in range(n):
            if ((matching_trainers[i] != [None]) and
                    (matching_trainers[less_matching_trainer] == [None] or
                    len(matching_trainers[i]) < len(matching_trainers[less_matching_trainer]))):
                less_matching_trainer = i
        if len(matching_trainers[less_matching_trainer]) == 0:
            remove_matched_index(matching_trainers, less_matching_trainer)
            alone_trainers += 1
            processed_trainer_count += 1
        else:
            min_matcher = matching_trainers[less_matching_trainer][0]
            for i in range(len(matching_trainers[less_matching_trainer])):
                if (len(matching_trainers[matching_trainers[min_matcher][i]]) < len(matching_trainers[min_matcher])):
                    min_matcher = matching_trainers[less_matching_trainer][i]
            remove_matched_index(matching_trainers, less_matching_trainer)
            remove_matched_index(matching_trainers, min_matcher)
            processed_trainer_count += 2
    return alone_trainers

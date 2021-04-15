from copy import deepcopy
from itertools import permutations


def get_shortest_times(times, n):
    shortest_times = deepcopy(times)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                time = shortest_times[i][k] + shortest_times[k][j]
                if (time < shortest_times[i][j]):
                    shortest_times[i][j] = time
    for i in range(n):
        # Returns empty list when a negative cycle is detected
        if (shortest_times[i][i] < 0):
            return []
    return shortest_times


def solution(times, time_limit):
    n = len(times)

    # Handle case when there is no bunny to save
    if n <= 2:
        return []

    bunnies = n - 2
    shortest_times = get_shortest_times(times, n)

    # If there is a negative cycle, we can always save all bunnies
    if len(shortest_times) == 0:
        return [i for i in range(n - 2)]

    # Now we test all permutations of the list of bunnies
    all_bunnies_permutations = permutations(range(1, 1 + bunnies))
    max_saved_bunnies = []
    for bunnies_permutation in all_bunnies_permutations:
        path = [0] + list(bunnies_permutation)
        path_time = 0

        # If we find a permutation to save them all, no need to continue futher
        if (len(max_saved_bunnies) == bunnies):
            return [i - 1 for i in max_saved_bunnies]

        # We travel the entire path to find which bunnies we can save
        saved_bunnies = []
        for i in range(bunnies):
            saved_bunnies.append(path[i + 1])
            path_time += shortest_times[path[i]][path[i + 1]]
            time_to_exit = shortest_times[path[i + 1]][bunnies + 1]

            # If we can exit at this stage, it means we can save these bunnies
            if path_time + time_to_exit <= time_limit:
                if len(saved_bunnies) > len(max_saved_bunnies):
                    max_saved_bunnies = deepcopy(saved_bunnies)
                elif len(saved_bunnies) == len(max_saved_bunnies):
                    max_saved_bunnies = min(
                        deepcopy(max_saved_bunnies),
                        deepcopy(saved_bunnies)
                    )

    # The list of bunnies need to be sorted to be the unique expected solution
    return [i - 1 for i in sorted(max_saved_bunnies)]

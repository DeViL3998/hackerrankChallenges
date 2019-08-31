def magic_square(arr):
    all_possible = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]], ]
    diff = []

    for possible in all_possible:
        cost = 0
        for i, j in list(zip(possible, arr)):
            for p, s in list(zip(i, j)):
                if p != s:
                    cost += abs(p - s)
            diff.append(cost)
    return min(diff)


print(magic_square([[8, 1, 5], [3, 5, 7], [4, 9, 2]]))

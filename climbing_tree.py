def climbingLeaderboard(scores, alice):
    uniq = list(reversed(sorted(set(scores))))
    i = len(alice) - 1
    j = 0
    arr = []
    while i >= 0:
        if j >= len(uniq) or uniq[j] <= alice[i]:
            arr.append(j + 1)
            i -= 1
        else:
            j += 1

    return arr[::-1]


print(climbingLeaderboard([100, 100, 50, 50, 40, 40, 20, 20, 10], [5, 25, 50, 120]))

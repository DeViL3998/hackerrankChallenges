def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple = count_orange = 0
    for i in apples:
        if s <= a + i <= t:
            count_apple += 1
    for i in oranges:
        if s <= b + i <= t:
            count_orange += 1
    print(count_apple)
    print(count_orange)


countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])

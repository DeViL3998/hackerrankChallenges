def construct_the_array(n, k, x):
    if x != 1:
        a, b = [0], [1]
    elif x == 1:
        a, b = [1], [0]
    for i in range(1, n):
        a.append(b[i-1])
        b.append(b[i-1]*(k-2) + a[i-1]*(k-1))
    print(a, b)
    return a[-1]


print(construct_the_array(4, 3, 2))
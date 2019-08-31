def between_2sets(arr, brr):
    count = 0
    for i in range(max(arr), min(brr)+1, max(arr)):
        if all([True if i % y == 0 else False for y in arr]):
            if all([True if x % i == 0 else False for x in brr]):
                count += 1
    return count


print(between_2sets([2, 4], [16, 32, 96]))

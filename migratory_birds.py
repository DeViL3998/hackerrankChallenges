from collections import Counter


def migratory_birds1(arr):
    return Counter(arr).most_common(1)[0][0]


def migratory_birds2(arr):
    counter = [0] * 6
    for m in arr:
        counter[m] += 1
    return counter.index(max(counter))


i = int(input())
check = list(map(int, input().split(' ')))
print(migratory_birds2(check))

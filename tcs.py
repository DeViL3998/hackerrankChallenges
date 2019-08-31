n, m = list(map(int, input().split(" ")))
arr = [ ]
count = count2 = 0
for i in range(n, m+1):
    for j in range(1, i//2 + 1):
        if i%j == 0:
            count += 1
    if count == 1:
        arr.append(i)
    count = 0
for i in arr:
    if i + 6 in arr:
        count2 += 1
print(count2)
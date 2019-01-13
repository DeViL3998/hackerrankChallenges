def count(amount, number, coins):

    table = [[0 for x in range(number)] for x in range(amount+1)]

    for i in range(number):
        table[0][i] = 1

    for i in range(1,amount+1):
        for j in range(number):

            x = table[i-coins[j]][j] if i-coins[j]>=0 else 0

            y = table[i][j-1] if j >=1 else 0

            table[i][j] = x + y

    return table[amount][number-1]

nm = list(map(int, input().split()))
amount = nm[0]
coins = list(map(int, input().split()))
print(count(amount, len(coins), coins))

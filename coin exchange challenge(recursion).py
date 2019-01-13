def nWays(money,coinCurr,coins):

    if money==0:
        return 1

    if money<0:
        return 0

    ways = 0

    for coin in range(coinCurr, len(coins)):
        ways += nWays(money-coins[coin], coin, coins)

    return ways

mn = list(map(int,input().split()))
money = mn[0]
coins= list(map(int, input().split()))

print(nWays(money,0,coins))

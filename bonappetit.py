def bon_appetit(bill, k, b):

    if (sum(bill)-bill[k])/2 == b:
        print("Bon Appetit")

    else:
        print(bill[k]//2)
# else


def bon_appetit2(bill, k, b):
    print("Bon Appetit" if (sum(bill)-bill[k]) // 2 else bill[k]/2)


print(bon_appetit([2, 2, 4], 2, 2))

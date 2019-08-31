def day_of_the_programmer(n):

    if n <= 1917:
        if n % 4 == 0:
            return "12.09."+str(n)
        else:
            return "13.09."+str(n)
    elif n >= 1919:
        if n % 4 == 0:
            if n % 100 == 0 and n % 400 != 0:
                return "13.09."+str(n)
            else:
                return "12.09."+str(n)
        else:
            return "13.09."+str(n)
    elif n == 1918:
        return "26.09.1918"

print(day_of_the_programmer(2017))
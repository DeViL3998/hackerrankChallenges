# gets timed out
def num_ways(arr, target, crr):
    count = 0
    brr = arr[:]
    if len(crr) == 0:
        for i in range(len(arr)):
            while brr[i] != target:
                if brr[i]-5 >= target:
                    brr[i] -= 5
                    count += 1
                elif brr[i]-2 >= target:
                    brr[i] -= 2
                    count += 1
                elif brr[i]-1 >= target:
                    brr[i] -= 1
                    count += 1
        return count
    else:
        for i in range(len(arr)):
            while brr[i] != target and count < min(crr):
                if brr[i] - 5 >= target:
                    brr[i] -= 5
                    count += 1
                elif brr[i] - 2 >= target:
                    brr[i] -= 2
                    count += 1
                elif brr[i] - 1 >= target:
                    brr[i] -= 1
                    count += 1
        return count


def equal(arr):
    crr = []
    for i in range(5):
        crr.append(num_ways(arr, min(arr) - i, crr))
    return min(crr)

# retry
def delta(target):
    brr = []
    for i in target:
        brr.append(i//5)            #counting 5
        brr.append((i%5)//2)        #counting 2
        brr.append(((i%5)%2)//1)    #counting 1
    return sum(brr)

def equal2(arr):
    c = []
    for i in range(5):
        c.append(delta([ x - y for x, y in list(zip(arr, [min(arr) - i] * len(arr)))]))
    return min(c)


print(equal2([53, 361, 188, 665, 786, 898, 447, 562, 272, 123, 229, 629, 670, 848, 994, 54, 822, 46, 208, 17, 449, 302, 466, 832, 931, 778, 156, 39, 31, 777, 749, 436, 138, 289, 453, 276, 539, 901, 839, 811, 24, 420, 440, 46, 269, 786, 101, 443, 832, 661, 460, 281, 964, 278, 465, 247, 408, 622, 638, 440, 751, 739, 876, 889, 380, 330, 517, 919, 583, 356, 83, 959, 129, 875, 5, 750, 662, 106, 193, 494, 120, 653, 128, 84, 283, 593, 683, 44, 567, 321, 484, 318, 412, 712, 559, 792, 394, 77, 711, 977, 785, 146, 936, 914, 22, 942, 664, 36, 400, 857]))

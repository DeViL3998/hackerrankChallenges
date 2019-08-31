def time_conversion(s):
    if s[-2:] == 'PM':
        t = int(s[:2]) + 12
        if t == 24:
            str1 = '12' + s[2:-2]
        else:
            str1 = str(t) + s[2:-2]
    else:
        t = int(s[:2])
        if t < 10:
            str1 = '0' + str(t) + s[2:-2]
        elif t == 12:
            str1 = '00' + s[2:-2]
        else:
            str1 = str(t) + s[2:-2]

    return str1



print(time_conversion('12:40:22PM'))
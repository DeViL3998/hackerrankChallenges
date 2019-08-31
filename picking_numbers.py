def picking_numbers(s):
    value = []
    for i in range(len(s)):
            value.append(s.count(s[i]) + s.count(s[i]+1))
    return max(value)


print(picking_numbers([4, 6, 5, 3, 3, 1]))

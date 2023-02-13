value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def RomanToDecimal(str):
    res = 0
    i = 0
    while i < len(str):
        s1 = value[str[i]]
        if i + 1 < len(str):
            s2 = value[str[i + 1]]
            if s1 >= s2:
                res += s1
            else:
                res += s2 - s1
                i += 1
        else:
            res += s1
        i += 1
    return res

print(RomanToDecimal("MCMIV"))
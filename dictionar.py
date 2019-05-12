def string (str2):
    a = 0
    e = 0
    u = 0
    i = 0
    o = 0
    for counter in range(len(str2)):
        if str2[counter] == "a":
            a = a + 1
        if str2[counter] == "e":
            e = e + 1
        if str2[counter] == "u":
            u = u + 1
        if str2[counter] == "i":
            i = i + 1
        if str2[counter] == "o":
            o = o + 1
    return (a,e,u,i,o)
str1 = str(input("enter string: "))
print(string(str1))
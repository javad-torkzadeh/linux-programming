def pasword (x):
    alpha = 1
    digit = 1
    special = 1
    if len(x) < 8 :
        return False
    y = x.split("?")
    if len(y) > 1:
        return False
    for i in x:
        if (i.isdigit()) == True:
            digit = digit + 1
        elif (i.isalpha()) == True:
            alpha = alpha + 1
        else :
            special = special + 1
        if digit > 1  and alpha > 1 and special > 1:
            return True
    return False
a = str(input("enter pasword: "))
print(pasword(a))
def mosalas (x,y,z):
    maximum = x
    if y > maximum  :
        maximum = y
    if z > maximum :
        maximum = z
        if maximum < x + y:
            return True
    if maximum == y:
        if maximum < x + z :
           return True
    if maximum == x:
        if maximum < y + z :
            return True
    return False
a = int (input("enter zel1:"))
b = int (input("enter zel2 : "))
c = int (input("enter zel3: "))
d = mosalas(a,b,c)
print(d)

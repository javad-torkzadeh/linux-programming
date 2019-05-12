def name (x):
    name2 = []
    name1 = x.split(",")
    for counter in range (len(name1)):
        name2.append(name1[len(name1) - counter - 1])
    return name2

a = str(input("enter string"))
print(name(a))
zrb = 1
b = 0
i = 0
while 2 :
    grade = input("enter grade (A,B,C,D or F) : ")
    grade = str (grade)
    counter = input("enter counter 2,3 or 5 :")
    counter = int (counter)
    done1 = input("enter done to finish :")
    done1 = str (done1)
    if grade == "a" :
        zrb = 4 * counter
    if grade == "b" :
        zrb = 3 * counter
    if grade == "c" :
        zrb = 2 * counter
    if grade == "d" :
        zrb = 1 * counter
    if grade == "f" :
        zrb = 0 * counter
    i = zrb + i
    b = counter + b

    if done1 == "done" :
        break

print(i/b)
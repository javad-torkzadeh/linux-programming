integer = input ("enter an integer")
integer = int (integer)
total = 0
gradecounter = 1
while gradecounter <= integer :
    grade = input("enter grade:")
    grade = int(grade)
    total = total+grade
    gradecounter = gradecounter+1
avg = total/integer
print("avrage is : {:10.4f}" .format(avg))

def printpattern(n):

     for counter in range(n//2):
         string = ""
         for counter2 in range(counter + 1):
             string = string + str(2*(counter2 + 1) )
         print(string)
a = int(input("enter number : "))
printpattern(a)
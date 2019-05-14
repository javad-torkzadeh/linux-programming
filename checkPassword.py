#def check_password (password):
 #   alpha = 1
  #  digit = 1
   # special = 1
    #lenth(password)
    #token_list = password.split("?")
    #if len(token_list) > 1:
     #   return False
    #
       #
        #else :
         #   special = special + 1
       # if digit > 1  and alpha > 1 and special > 1:
        #    return True
    #return False
def length (lent):
    if len(lent) > 8:
        return True
    else:
        return False
def digit (dig):
    digit = 0
    for character in dig:
      if character.isdigit():
          for character2 in dig:
              if character2.isalpha():
                 return True
def question_mark (mark):
    for counter in mark:
        if counter == "?":
            return False
    return True
password = str(input("Enter pasword: "))
if length(password) == True and digit(password) == True and question_mark(password):
       print("password is true ")
else:
    print("password is false")
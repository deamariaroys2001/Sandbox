"""
  Password_check
"""
MIN_LENGTH = 5
Password_check=True

print("Please enter a password: ")
password = input(" ")
while Password_check :
 if len(password) > MIN_LENGTH:
  for n in range(0,len(password),1):
     print("*",end=' ')
  Password_check =False
 else:
    print("Your password must be atleast", MIN_LENGTH,
          "characters .")
    print("Please enter a new password: ")
    password = input(" ")



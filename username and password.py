# username and password authentication
# code 100% written by me
# My social media:
# x.com/ismatronics
# github.com/ismatronics
# instagram.com/ismatronics
# youtube.com/@ismatronics

print("Code written by ismatronics")
print("")

#define username
username = str(input("Username: "))

#confirm username
while (str(input("Confirm username: "))) != username:
    print("Usernames do not match")
    #in case it fails it makes the user repeat it twice for extra security
    str(input("Confirm username: "))
    print("Repeat again for extra security")
#defines de password
password = str(input("Password: "))
while (str(input("Confirm password: "))) != password:
    print("Paswords do not match")
    #in case it fails it makes the user repeat it twice for extra security
    str(input("Confirm password: "))
    print("Repeat again for extra security")
#when sign up is succesful it prints the next message
print("User succesfully signed")
print("")
#the next code makes the user log in with his new account
print("Log in")
#it makes the user enter his username
usernameguess = str(input("Username: "))
#in case the user writes the username wrong it makes it try again
while (str(usernameguess)) != username:
    print("This username does not exist", "Try again")
    usernameguess = str(input("Username: "))
#it makes the user input his password
passwordguess = str(input("Password: "))
#in case the user writes the password wrong it makes it try again
while (str(passwordguess)) != password:
    print("Wrong password", "Try again")
    passwordguess = str(input("Password: "))
#if the user writes the password right it print the next message
print("Log in succesful")

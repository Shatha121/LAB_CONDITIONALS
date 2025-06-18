username = input("Enter your username: ")
Email = input("Enter your Email: ")



if len(username) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")
elif Email.find("@gmail") == -1:
    print("the email is not valid , please provide a valid email .")
else:
    print(f"welcome {username} , you registered with the email {Email} !")

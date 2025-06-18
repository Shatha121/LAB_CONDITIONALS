username = input("Enter your username: ")
Email = input("Enter your Email: ")



if len(username) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")
elif not Email.endswith("@gmail.com") or Email.find("@") == 0 or Email.count("@") != 1:
    print("the email is not valid , please provide a valid email .")

else:
    print(f"welcome {username} , you registered with the email {Email} !")

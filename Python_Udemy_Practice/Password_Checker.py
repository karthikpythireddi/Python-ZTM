
username = input("Enter your user name:")

passwrd = input("Enter your password:")

password_length = len(passwrd)

hiddden_password = '*' * password_length

print(f"Hey {username}, your password {hiddden_password} is {password_length} letters long")


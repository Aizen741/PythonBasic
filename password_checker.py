correct_password = "1234"

password = input("Enter the password here: ")

while correct_password != password:
    password = input("Wrong password Enter again:")

print("Logged in.")
correct_password = "1234"
name = input("Enter your name:")
password = input("Enter the password here: ")

while correct_password != password:

    password = input("Wrong password please Enter again:")

message = "Hi %s you are logged in" % name
print(message)


correct_password = "1234"
name = input("Enter your name:")
password = input("Enter the password here: ")

while correct_password != password:

    password = input("Wrong password please Enter again:")

message = "Hi %s you are logged in" % name
print(message)


true_data = "Alpha234"

Data = input("Enter your batch number : ")

while Data != true_data:
    Data = input("Wrong id , Re-enter :")

message1 ="%s,you now have the access into the SkyNet corp." % name
print(message1)


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
        if smallest is None:
            smallest = number
        elif number < smallest:
            print("Smallest",number)
        if largest is None:
            largest = number
        elif number > largest:
            print("Largest ",number)


    except:
        print("Invalid input")
        continue




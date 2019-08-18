#Factorials
n = int(input("Enter the number : "))
def factorial(n):
    factoriallist = []
    for i in range(1,n+1):
        if n%i ==0:
            factoriallist = factoriallist +[i]
    return factoriallist
print(factorial(n))
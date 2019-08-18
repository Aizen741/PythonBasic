#Factorials
n = int(input("Enter the number : "))
def factorial(n):
    if n <= 0:
        return (1)
    else:
        val = n * factorial(n-1)
        return (val)

print(factorial(n))
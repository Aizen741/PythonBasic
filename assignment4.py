hrs = input("Enter Hours:")
rate = input("Enter rate:")
x = float(hrs)
y = float(rate)
def computepay(x, y):
    if(x <= 40):
        gross = x * y
        return (gross)
    else:
        gross = x * y
        total = (x - 40.0) * (y * 0.5)
        return (gross + total)

p = computepay(x, y)
print("Pay",p)
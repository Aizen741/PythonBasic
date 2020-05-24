
hrs = input("Enter Hours:")
rate = input("Enter rate:")
x = float(hrs)
y = float(rate)
if(x <= 40):
    gross = x * y
    print(gross)
else:
    gross = x * y
    total = (x - 40.0) * (y * 0.5)
    print(gross + total)

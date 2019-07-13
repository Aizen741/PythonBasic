
def myfunc(*args):
    even = [ ]
    for item in args:
        if item %2 == 0:
            even.append(item)
    return  even
print(myfunc(3,44.54,1,2,34,5))
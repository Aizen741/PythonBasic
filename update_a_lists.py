# Updating a list
def update(l,i,v):
    if i >= 0 and i < len(l):
        l[i] = v
        return (True)
    else:
        v = v + 1
        return (False)


ns = [2,3,4,5]
z = 4

print(update(ns,3,z))

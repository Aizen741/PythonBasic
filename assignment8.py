fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

words = [line.rstrip().split() for line in fh]

for item in words:
    for word in item:
        if word not in lst:
            lst.append(word)

print (sorted(lst))
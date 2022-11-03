f = open("text.txt", "r")
data = f.readlines()
tail = data[-2:]
print(''.join(tail))

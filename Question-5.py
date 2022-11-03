f = open("text.txt", "r")
data = f.readlines()
data = [x.strip() for x in data]
print(data)

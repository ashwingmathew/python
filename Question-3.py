f = open("text.txt", "a")
f.write("Hi,Welcome.")
f.close()
f = open("text.txt", "r")
print(f.read())

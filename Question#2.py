word = "hello"
res = {i : word.count(i) for i in set(word)}
print (str(res))

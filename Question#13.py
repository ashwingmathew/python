num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
print(sub_lists(num))

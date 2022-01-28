def greater_than_index(l, n):
    for i in l:
        if i >= n:
            return l.index(i)
    return

list = [1.1, 2.2, 3.3, 4.4, 5.5]
print(list)
print(greater_than_index(list, 100.5))
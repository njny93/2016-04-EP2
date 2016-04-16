def linearSearch(l, e):
    for i in range(len(l)):
        if l[i] == e:
            return i
    return None

a = [5, 4, 7, 2, 3, 6, 9, 1]

print(linearSearch(a, 3))

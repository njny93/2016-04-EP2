def sort(l):
    for i in range(len(l)):
        x = l.pop(i)
        inserted = False
        for j in range(i-1, -1, -1):
            if x > l[j]:
                l.insert(j+1, x)
                inserted = True
                break
        if not inserted:
            l.insert(0, x)

a = [3, 76, 2, 9, 54, 22, 18, 39]
sort(a)
print(a)

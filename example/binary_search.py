def bsearch(l, e):
    lo = 0
    hi = len(l)-1
    while lo < hi:
        mid = (hi+lo)//2
        if e < l[mid]:
            hi = mid
        elif e > l[mid]:
            lo = mid+1
        else:
            return mid
    return -1

a = [2, 3, 4, 6, 17, 39, 42]
print(bsearch(a, 17))

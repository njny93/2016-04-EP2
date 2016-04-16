def create(item):
    return (item, None)

def append(l, item):
    if l[1] == None:
        l_list = [l[0], (item, None)]
        return tuple(l_list)
    else:
        l_list = [l[0], append(l[1], item)]
        return tuple(l_list)

def find(l, item):
    if l[0] == item:
        return item
    elif l[1] == None:
        return None
    else:
        return find(l[1], item)

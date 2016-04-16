def create(item):
    return [item, None]

def append(l, item):
    if l[1] == None:
        l[1] = [item, None]
    else:
        append(l[1], item)

def find(l, item):
    if l[0] == item:
        return item
    elif l[1] == None:
        return None
    else:
        return find(l[1], item)

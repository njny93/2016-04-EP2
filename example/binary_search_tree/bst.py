def create(item):
    return [item, None, None]

def add(tree, item):
    if tree[0] > item:  # left
        if tree[1] == None:
            tree[1] = [item, None, None]
            return True
        else:
            add(tree[1], item)
    elif tree[0] < item:    # right
        if tree[2] == None:
            tree[2] = [item, None, None]
            return True
        else:
            add(tree[2], item)
    else:
        return False

def find(tree, item):
    if tree[0] > item:  # left
        if tree[1] == None:
            return None # not found
        else:
            return find(tree[1], item)
    elif tree[0] < item:    # right
        if tree[2] == None:
            return None # not found
        else:
            return find(tree[2], item)
    else:
        return item

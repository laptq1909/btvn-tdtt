class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_count = 0
        self.count = 1
def insert(node, val):
    if val == node.val:
        node.count += 1
        return node.left_count
    elif val < node.val:
        node.left_count += 1
        if node.left:
            return insert(node.left, val)
        else:
            node.left = Node(val)
            return 0
    else:  # val > node.val
        smaller = node.left_count + node.count
        if node.right:
            return smaller + insert(node.right, val)
        else:
            node.right = Node(val)
            return smaller
def countSmaller(nums):
    res = []
    root = None

    for num in reversed(nums):
        if root is None:
            root = Node(num)
            res.append(0)
        else:
            res.append(insert(root, num))

    return res[::-1]
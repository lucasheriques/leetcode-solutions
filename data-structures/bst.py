# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self, node):
        return node.left == None and node.right == None

    def insert(self, value):
        root = self
        if value < root.value:
            if root.left is None:
                root.left = BST(value)
            else:
                root.left.insert(value)
        else:
            if root.right is None:
                root.right = BST(value)
            else:
                root.right.insert(value)
        return self

    def contains(self, value):
        node = self
        if value == node.value:
            return True
        elif value < node.value:
            if node.left is None:
                return False
            else:
                return node.left.contains(value)
        else:
            if node.right is None:
                return False
            else:
                return node.right.contains(value)
        return False

    def getMinValue(self):
        node = self
        while node.left is not None:
            node = node.left
        return node.value

    def remove(self, value, parent=None):
        node = self
        while node is not None:
            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            else:
                if node.left is not None and node.right is not None:
                    node.value = node.right.getMinValue()
                    node.right.remove(node.value, node)
                elif parent is None:
                    if node.left is not None:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right is not None:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else:
                        node.value = None
                elif parent.left == node:
                    parent.left = node.left if node.left is not None else node.right
                elif parent.right == node:
                    parent.right = node.left if node.left is not None else node.right
                break

        return self


test4 = BST(10).insert(5).insert(15).insert(22).insert(17).insert(34) \
    .insert(7).insert(2).insert(5).insert(1).insert(35).insert(27).insert(16) \
    .insert(30) \
    .remove(22)

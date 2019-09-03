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
        created = False
        while not created:
            if value < root.value:
                if root.left is None:
                    root.left = BST(value)
                    created = True
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = BST(value)
                    created = True
                else:
                    root = root.right
        return self

    def contains(self, value):
        node = self
        while node is not None:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def is_leaf(self, node):
        return node.left is None and node.right is None

    def remove(self, value):
        root = self
        removed = False
        while not removed and root is not None:
            if value == root.value:
                removed = True
                if self.is_leaf(root):
                    root = None

                elif root.left:
                    if root.right:
                        new = root.right
                        while new.left is not None:
                            new = new.left
                        root.value = new.value
                        self.remove(new)

                    else:
                        root.value = root.left.value
                        root.left = None

                elif root.right:
                    root.value = root.right.value
                    root.right = None

            elif value < root.value:
                root = root.left

            else:
                root = root.right
        return self


test4 = BST(10).insert(5).insert(15).insert(22).insert(17).insert(34) \
    .insert(7).insert(2).insert(5).insert(1).insert(35).insert(27).insert(16) \
    .insert(30) \
    .remove(22)

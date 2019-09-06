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

    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def remove(self, value, parent_node=None):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left and current_node.right:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                elif parent_node.left == current_node:
                    parerent_node.left = current_node.left if current_node.left else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left else current_node.right

        return self


test4 = BST(10).insert(5).insert(15).insert(22).insert(17).insert(34) \
    .insert(7).insert(2).insert(5).insert(1).insert(35).insert(27).insert(16) \
    .insert(30) \
    .remove(22)

def findClosestValueInBst(tree, target):
    # Write your code here.
    return find(tree, target, tree.value)


def find(tree, target, closest):
    closest = tree.value if abs(
        tree.value - target) < abs(closest - target) else closest

    if tree.value == target:
        return tree.value

    elif tree.value > target:
        if tree.left:
            return find(tree.left, target, closest)
        return closest

    else:
        if tree.right:
            return find(tree.right, target, closest)
        return closest

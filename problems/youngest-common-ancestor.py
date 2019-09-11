# You're given three inputs, all of which are instances of a class that have an
# "ancestor" property pointing to their youngest ancestor. The first input is
# the top ancestor in an ancestral tree (i.e., the only instance that has no
# ancestor), and the other two inputs are descendants in the ancestral tree.
# Write a function that returns the youngest common ancestor to the two
# descendants.


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getAncestorDepth(descendantOne, topAncestor)
    depthTwo = getAncestorDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return findAncestor(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return findAncestor(descendantTwo, descendantOne, depthTwo - depthOne)


def getAncestorDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        descendant = descendant.ancestor
        depth += 1
    return depth


def findAncestor(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant

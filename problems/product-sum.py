# Write a function that takes in a "special" array and returns its product sum. A
# "special" array is a non-empty array that contains either integers or other
# "special" arrays. The product sum of a "special" array is the sum of its
# elements, where "special" arrays inside it should be summed themselves and then
# multiplied by their level of depth. For example, the product sum of [x, y] is x
# + y; the product sum of [x, [y, z]] is x + 2y + 2z.


# O(N), where N is the total number of elements (including in the subarrays) | O(D), where D is the max subarray depth
def productSum(array, depth=1):
    sum = 0
    for i in range(len(array)):
        if isinstance(array[i], int):
            sum += array[i]
        else:
            sum += productSum(array[i], depth + 1)
    return sum * depth


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    ans = [0, float('inf')]

    i = j = 0

    while i < len(arrayOne) and j < len(arrayTwo):
        if abs(ans[0] - ans[1]) > abs(arrayOne[i] - arrayTwo[j]):
            ans[0], ans[1] = arrayOne[i], arrayTwo[j]

            if ans[0] - ans[1] == 0:
                return ans

        if arrayOne[i] <= arrayTwo[j]:
            i += 1
        else:
            j += 1

    return ans

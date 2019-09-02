def selection_sort(nums):
    length = len(nums)
    for i in range(length):
        smallest_index = i
        for j in range(i + 1, length):
            if nums[j] < nums[smallest_index]:
                smallest_index = j

        if i != smallest_index:
            nums[i], nums[smallest_index] = nums[smallest_index], nums[i]

    return nums


def bubble_sort(array):
    is_sorted = False
    counter = 0
    while is_sorted == False:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        counter += 1  # small optimization

    return array


print(selection_sort([193, 33, 2, 52, 106, 73, 1, 9, 7, 4, 3, 5, 1823]))
print(bubble_sort([193, 33, 2, 52, 106, 73, 1, 7, 9, 4, 3, 5, 1823]))

# time complexity:O(n^2)
# space complexity:O(1)
def bubbleSort(array, len):
    for i in range(len):
        for j in range(1, len):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
        print("round {}, result {}".format(i, array))

# time complexity:
# spcae complecity:
def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        greater = [key for key in array[1:] if key > pivot]
        less = [key for key in array[1:] if key < pivot]
        equal = [key for key in array[1:] if key == pivot]
        return quickSort(less) + equal + [pivot] + quickSort(greater)

if __name__ == "__main__":
    array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    # bubbleSort(array, len(array))
    array = quickSort(array)
    print(array)
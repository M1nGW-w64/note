def directInsertSort(array, len):
    for i in range(1, len):
        if array[i] < array[i-1]:
            # find the insert pos
            for j in range(i - 1, -1, -1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        print("round {}, result {}".format(i, array))

def binaryInsertSort(array, len):
    for i in range(1, len):
        temp = array[i]

        # find the insert pos
        low, high = 0, i-1
        while low <= high:
            mid = int((high + low) / 2)
            if array[mid] < temp:
                low = mid + 1
            else:
                high = mid - 1

        for j in range(i, low, -1):
            array[j] = array[j - 1]
        array[high + 1] = temp
        print("round {}, result {}".format(i, array))

def shellSort(array, len):
    step = int(len/2)

    while step > 0:
        for i in range(step, len):
            temp = array[i]
            j = i
            while j >= step and array[j - step] > temp:
                array[j] = array[j - step]
                j -= step
            array[j] = temp
        print("step {}, result {}".format(step, array))
        step = int(step/2)

if __name__ == "__main__":
    array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    # directInsertSort(array, len(array))
    # binaryInsertSort(array, len(array))
    # shellSort(array, len(array))
    print(array)

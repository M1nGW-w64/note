# time complexity:O(n^2)
# space complexity:O(1)
def selectSort(array, len):
    for i in range(len):
        min = i
        for j in range(i + 1, len):
            if array[j] < array[min]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
        print("round {}, result {}".format(i, array))

# time complexity:O(nlogn)
def heapSort(array, len):

    def adjustHeap(array, len, key):
        temp = array[key]
        child = 2 * key + 1

        while child < len:
            # have right-child, and lager then left-child, then turn to the r-child
            if child + 1 < len and array[child] < array[child + 1]:
                child += 1
            if array[child] <= temp:
                break
            array[key] = array[child]
            key = child
            child = 2 * key + 1
        array[key] = temp
    
    # build heap
    for i in range((len - 2)//2, -1, -1):
        adjustHeap(array, len, i)
    
    # pop front elem, and adjust heap
    for i in range(len - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        adjustHeap(array, i, 0) 


if __name__ == "__main__":
    array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    # selectSort(array, len(array))
    heapSort(array, len(array))
    print(array)
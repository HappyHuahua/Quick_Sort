def quick_sort_once(array, low, high):
    save = array[low]
    while low < high:
        while low < high and save <= array[high]:
            high = high - 1
        array[low] = array[high]
        while low < high and save >= array[low]:
            low = low + 1
        array[high] = array[low]
    array[low] = save
    return low


def quick_sort(array, low, high):
    if low < high:
        local = quick_sort_once(array, low, high)
        if low < local:
            quick_sort(array, low, local - 1)
        if local < high:
            quick_sort(array, local + 1, high)
    return array


if __name__ == '__main__':
    arr = input("Input array: ")
    kk = [int(n) for n in arr.split()]
    kk = quick_sort(kk, 0, len(kk) - 1)
    print(kk)

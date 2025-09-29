def first_occurrence(arr, element):

    low = 0
    high = len(arr) - 1

    while low < high:
        mid = int((low + high)/2)

        if element > arr[mid]:
            low = mid + 1
        else:
            high = mid

    if element == arr[low]:
        return low
    else:
        return -1


if __name__ == "__main__":
    input_arr = [ 1, 3, 3, 3, 4, 4, 6, 6, 6, 6, 7, 7, 7, 8, 8, 11, 15, 22]

    target = 3

    index = first_occurrence(input_arr, target)

    print(f"first occurrence of element {target} is at index {index}")
def last_occurrence(arr, element):

    low = 0
    high = len(arr) - 1

    while low < high:
        # The intuition here is you want to move the search towards the rightmost occurrence
        # So, you need the midpoint to bias slightly towards the right, which justifies the +1.
        mid = int((low + high + 1) / 2)

        if element < arr[mid]:
            high = mid-1
        else:
            low = mid

    if element == arr[low]:
        return low
    else:
        return -1


if __name__ == "__main__":
    input_arr = [ 1, 3, 3, 3, 4, 4, 6, 6, 6, 6, 7, 7, 7, 8, 8, 11, 15, 22]

    target = 3

    index = last_occurrence(input_arr, target)

    print(f"last occurrence of element {target} is at index {index}")
def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i

    return -1

if __name__ == "__main__":
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7

    print(f"element found at index: {linear_search(input_arr, target)}")
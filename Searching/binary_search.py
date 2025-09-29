import time
from datetime import datetime

def binary_search(arr, element):

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = int((low + high)/2)

        if element < arr[mid]:
            high = mid-1
        elif element > arr[mid]:
            low = mid+1
        else:
            return mid

    return -1

if __name__ == "__main__":
    count = int(input("Enter the number of elements: "))

    # Get elements one by one
    input_arr = []
    for index in range(count):
        num = int(input(f"Enter the element {index + 1}: "))
        input_arr.append(num)

    target = int(input("Enter the element to be searched: "))

    # Record time before and after sorting
    start_time = time.time()
    index = binary_search(input_arr, target)
    end_time = time.time()

    # Convert timestamps to human-readable format
    start_readable = datetime.fromtimestamp(start_time).strftime("%H:%M:%S")
    end_readable = datetime.fromtimestamp(end_time).strftime("%H:%M:%S")

    # time taken to sort the array
    execution_time = end_time - start_time

    print(f"Element found at index {index} in {execution_time:.6f} seconds")
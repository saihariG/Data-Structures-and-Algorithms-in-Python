import time
from datetime import datetime

def bubble_sort(arr):
    n = len(arr)

    # traverse through the array
    for i in range(n):
        # Last i elements are already in place, so inner loop goes till n-i-1
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

if __name__ == '__main__':
    count = int(input("Enter the number of elements: "))

    # Get elements one by one
    input_arr = []
    for index in range(count):
        num = int(input(f"Enter the element {index+1}: "))
        input_arr.append(num)

    print("Unsorted array: ", input_arr)

    #Record time before and after sorting
    start_time = time.time()

    sorted_arr = bubble_sort(input_arr)

    end_time = time.time()

    print("Sorted array: ", sorted_arr)


    # Convert timestamps to human-readable format
    start_readable = datetime.fromtimestamp(start_time).strftime("%H:%M:%S")
    end_readable = datetime.fromtimestamp(end_time).strftime("%H:%M:%S")

    #time taken to sort the array
    execution_time = end_time - start_time

    print(f"Execution time: {execution_time:.6f} seconds") # formatted to 6 decimal places
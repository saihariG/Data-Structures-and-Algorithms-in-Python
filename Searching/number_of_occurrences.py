from first_occurrence import first_occurrence
from last_occurrence import last_occurrence

def number_of_occurrences(arr, element):
    first = first_occurrence(arr, element)
    last = last_occurrence(arr, element)

    if first == -1:
        return -1
    else:
        return last - first + 1

if __name__ == "__main__":
    input_arr = [1, 3, 3, 3, 4, 4, 6, 6, 6, 6, 7, 7, 7, 8, 8, 11, 15, 22]

    target = 6

    count = number_of_occurrences(input_arr, target)

    print(f"element {target} occurred {count} times")
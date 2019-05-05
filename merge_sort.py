from __future__ import print_function
import time
from oscgrain import oscgrain

def merge_sort(collection):
    """Pure implementation of the merge sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_sort([])
    []

    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    print("Splitting ",collection)
    length = len(collection)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
                print(collection[k])
                oscgrain(30*collection[k]) #multiply freq 
                time.sleep(0.1) #introduce a delay  
            else:
                collection[k] = right_half[j]
                j += 1
                print(collection[k])
                oscgrain(30*collection[k]) #multiply freq 
                time.sleep(0.1) #introduce a delay  
            k += 1

        while i < left_length:
            collection[k] = left_half[i]
            print(collection[k])
            oscgrain(30*collection[k]) #multiply freq 
            time.sleep(0.1) #introduce a delay              
            i += 1
            k += 1

        while j < right_length:
            collection[k] = right_half[j]
            print(collection[k])
            oscgrain(30*collection[k]) #multiply freq 
            time.sleep(0.1) #introduce a delay  
            j += 1
            k += 1
    print("Merging ",collection)
    return collection


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(merge_sort(unsorted))
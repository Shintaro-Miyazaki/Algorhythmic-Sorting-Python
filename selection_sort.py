from __future__ import print_function
import time
from oscgrain import oscgrain

def selection_sort(collection):
    """Pure implementation of the selection sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending


    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
            print(collection[k], collection[least])
            #SONIFICTAION
            oscgrain(30*collection[k])
            time.sleep(0.1) #introduce delay
            oscgrain(30*collection[least])
        collection[least], collection[i] = (
            collection[i], collection[least]
        )
        print(collection[least], collection[i])
        #SONIFICTAION
        oscgrain(30*collection[least])
        time.sleep(0.1) #introduce delay
        oscgrain(30*collection[i])
    return collection

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(selection_sort(unsorted))
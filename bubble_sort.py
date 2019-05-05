from __future__ import print_function
import time
from oscgrain import oscgrain

def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:    
    >>> bubble_sort([-23,0,6,-4,34])
    [-23,-4,0,6,34]
    """
    length = len(collection)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if collection[j] > collection[j+1]:
                swapped = True
                #SONIFICTAION
                print(collection[j], collection[j+1])
                oscgrain(30*collection[j]) #multiply freq 
                time.sleep(0.1) #introduce a delay  
                oscgrain(30*collection[j+1]) #multiplyfreq 
                collection[j], collection[j+1] = collection[j+1], collection[j]    
                print(collection[j], collection[j+1])
                oscgrain(30*collection[j]) #multiplyfreq 
                time.sleep(0.1) #introduce a delay  
                oscgrain(30*collection[j+1]) #multiplyfreq 
        if not swapped: break  # Stop iteration if the collection is sorted.
    return collection

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    user_input = raw_input('Enters separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort(unsorted)) 
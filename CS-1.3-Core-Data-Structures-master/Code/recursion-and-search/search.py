#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    if index >= len(array):
        return None

    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)
        

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests

    leftIndex = 0
    rightIndex = len(array) - 1

    while leftIndex <= rightIndex:
        midIndex = (rightIndex + leftIndex) // 2
        if array[midIndex] == item:
            return midIndex
        elif item < array[midIndex]:
            rightIndex = midIndex - 1
        elif item  > array[midIndex]:
            leftIndex = midIndex + 1
    return None



def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

    if left == left:
        left = 0

    if right == right:
        right = 0

    if right >= left:

        middle = left + right // 2

        if array[middle] == item:
            return middle
        elif array[middle] > item:
            return binary_search_recursive(array, item, left, middle - 1)
        elif array[middle] < item:
            return binary_search_recursive(array,item,middle + 1, right)
    return None


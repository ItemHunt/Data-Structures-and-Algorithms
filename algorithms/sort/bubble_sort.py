# Bubble Sort - O(n^2)
def bubble_sort(lst):
    """
    This function sorts a given list of numbers using the Bubble Sort algorithm.

    Args:
    lst: An unsorted list of numbers.

    Returns:
    The sorted list of numbers in ascending order.
    """

    # Get the length of the list
    n = len(lst)

    # Traverse through all list elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    # Return the sorted list
    return lst

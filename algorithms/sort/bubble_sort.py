'''
Bubble Sort - O(n^2)

If you want a video about this algorithm instead, I recommend this video by Derrick Sherrill
https://youtu.be/g_xesqdQqvA
'''

def bubble_sort(lst):
    # Get the length of the list
    n = len(lst)

    # Traverse through all the elements of the list
    for i in range(n):

        # Traverse the list from 0 to n-i-1 as the last i elements are already in place
        for j in range(0, n-i-1):

            # Swap if the element found is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    # Return the sorted list
    return lst


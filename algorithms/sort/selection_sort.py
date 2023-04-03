# Selection Sort - O(n^2)
def selection_sort(lst):
    # iterate through the whole list
    for i in range(0, len(lst)):
        # assign the current index to the variable cur_idx
        cur_idx = i

        # iterate through the unsorted part of the list
        for j in range(i + 1, len(lst)):
            # if the value at the current index is greater than the value at index j
            if lst[cur_idx] > lst[j]:
                # update cur_idx to j
                cur_idx = j

        # swap the values at i and cur_idx
        lst[i], lst[cur_idx] = lst[cur_idx], lst[i]

    return lst

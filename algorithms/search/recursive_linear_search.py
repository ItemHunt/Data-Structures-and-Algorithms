# Linear Search - O(n)
def recursive_linear_search(arr, target):
    """
    Recursive implementation of linear search algorithm to find the index of target in arr.
    Returns -1 if target is not found in arr.
    """
    # Base case: if arr is empty, target is not found
    if not arr:
        return -1
    
    # Base case: if the first element of arr is the target, return its index
    if arr[0] == target:
        return 0
    
    # Recursive case: search the rest of arr for the target
    index = recursive_linear_search(arr[1:], target)
    
    # If target is found in the rest of arr, adjust the index to account for the sliced portion
    if index != -1:
        index += 1
    
    return index

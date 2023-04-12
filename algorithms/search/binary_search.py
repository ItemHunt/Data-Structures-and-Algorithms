# Binary Search - O(log n)
def binary_search(lst, target):
    # Set left and right indices
    left = 0
    right = len(lst) - 1
    
    # Loop until left and right pointers cross each other
    while left <= right:
        # Calculate middle index
        mid = (left + right) // 2
        
        # Check if target is at mid index
        if lst[mid] == target:
            return mid
        # If target is greater than mid element, ignore left half
        elif lst[mid] < target:
            left = mid + 1
        # If target is smaller than mid element, ignore right half
        else:
            right = mid - 1
    
    # If target is not found, return -1
    return -1

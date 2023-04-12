# Recursive Binary Search - O(log n)
def binary_search_recursive(arr, target):
    # base case: if array is empty or target is not in array
    if not arr:
        return -1
    
    # find the middle index of the array
    mid = len(arr) // 2
    
    # if the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    
    # if the middle element is greater than target, search the left half of the array
    elif arr[mid] > target:
        return binary_search_recursive(arr[:mid], target)
    
    # if the middle element is less than target, search the right half of the array
    else:
        result = binary_search_recursive(arr[mid+1:], target)
        if result == -1:
            return -1
        else:
            return mid + 1 + result
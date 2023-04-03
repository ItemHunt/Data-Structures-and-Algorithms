# Linear Search - O(n)
def linear_search(arr, target):

    # Iterate through the array and compare each element to the target value
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    # Target value not found in array
    return -1

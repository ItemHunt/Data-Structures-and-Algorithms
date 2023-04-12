# Bucket Sort - O(n)
def bucket_sort(lst):
    # Find the maximum value in the list and calculate the bucket size
    max_value = max(lst)
    bucket_size = max_value / len(lst)

    # Create an empty list of buckets
    buckets = [[] for _ in range(len(lst))]

    # Put each element in its corresponding bucket
    for num in lst:
        index = int(num / bucket_size)
        if index >= len(buckets):
            index = len(buckets) - 1
        buckets[index].append(num)

    # Sort each bucket individually
    for i in range(len(lst)):
        buckets[i] = insertion_sort(buckets[i])

    # Concatenate the sorted buckets and return the result
    return [num for bucket in buckets for num in bucket]

def insertion_sort(lst):
    # Traverse through all list elements
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        # Move elements of the list greater than key to one position ahead of their current position
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

    # Return the sorted list
    return lst
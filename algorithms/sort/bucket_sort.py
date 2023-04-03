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
        buckets[index].append(num)

    # Sort each bucket individually
    for i in range(len(lst)):
        buckets[i] = insertion_sort(buckets[i])

    # Concatenate the sorted buckets and return the result
    return [num for bucket in buckets for num in bucket]

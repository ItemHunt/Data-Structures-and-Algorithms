'''
Merge Sort - O(n * log(n))
Divide and Conquer Algorithm
Considered as optimal running time for comparison based algorithms

If you want a video about this algorithm instead, I recommend this video by FelixTechTips
https://youtu.be/cVZMah9kEjI?si=2f8YtZ9zhcrtc74j
'''

def merge_sort(arr):
    """
    Perform a merge sort on a list.

    Args:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.

    This function uses the merge sort algorithm to sort a list in ascending order.
    Merge sort is a divide-and-conquer algorithm that splits the list into two halves,
    sorts them separately, and then merges them.
    """

    # Base case: a list of zero or one elements is sorted by definition
    if len(arr) <= 1:
        return arr

    # Recursive case: split the list into two halves and sort them
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.

    Args:
    left (list): The first sorted list.
    right (list): The second sorted list.

    Returns:
    list: The merged sorted list.
    """

    merged = []
    left_index = 0
    right_index = 0

    # Merge smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in either list, add them to the merged list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

'''
C++ Version of Merge Sort
-------------------------
#include <vector>

/**
 * Merge two sorted vectors into one sorted vector.
 *
 * @param left The first sorted vector.
 * @param right The second sorted vector.
 * @return The merged sorted vector.
 */
std::vector<int> merge(std::vector<int> left, std::vector<int> right) {
    std::vector<int> merged;
    int left_index = 0, right_index = 0;

    // Merge smaller elements first
    while (left_index < left.size() && right_index < right.size()) {
        if (left[left_index] <= right[right_index]) {
            merged.push_back(left[left_index++]);
        } else {
            merged.push_back(right[right_index++]);
        }
    }

    // If there are remaining elements in either vector, add them to the merged vector
    while (left_index < left.size()) {
        merged.push_back(left[left_index++]);
    }
    while (right_index < right.size()) {
        merged.push_back(right[right_index++]);
    }

    return merged;
}

/**
 * Perform a merge sort on a vector.
 *
 * @param arr The vector to be sorted.
 * @return The sorted vector.
 *
 * This function uses the merge sort algorithm to sort a vector in ascending order.
 * Merge sort is a divide-and-conquer algorithm that splits the vector into two halves,
 * sorts them separately, and then merges them.
 */
std::vector<int> merge_sort(std::vector<int> arr) {
    // Base case: a vector of zero or one elements is sorted by definition
    if (arr.size() <= 1) {
        return arr;
    }

    // Recursive case: split the vector into two halves and sort them
    int mid = arr.size() / 2;
    std::vector<int> left_half(arr.begin(), arr.begin() + mid);
    std::vector<int> right_half(arr.begin() + mid, arr.end());

    left_half = merge_sort(left_half);
    right_half = merge_sort(right_half);

    // Merge the sorted halves
    return merge(left_half, right_half);
}
'''
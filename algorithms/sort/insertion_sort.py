'''
Insertion Sort - O(n^2)

If you want a video about this algorithm instead, I recommend this video by FelixTechTips
https://www.youtube.com/watch?v=R_wDA-PmGE4
'''

def insertion_sort(unordered_list):
    # Initialize an ordered list with the first element from the unordered list
    ordered_list = [unordered_list[0]]

    # Iterate through each element of the unordered list
    for i in range(1, len(unordered_list)):
        # Compare the current element of the unordered list to each element in the ordered list
        for j in range(len(ordered_list) - 1, -1, -1):
            # If the current element of the unordered list is greater than the element in the ordered list,
            # insert the element at the next index of the ordered list and break out of the loop
            if ordered_list[j] < unordered_list[i]:
                ordered_list.insert(j + 1, unordered_list[i])
                break
            # If the current element of the unordered list is smaller than all elements in the ordered list,
            # insert the element at the beginning of the ordered list and break out of the loop
            elif j == 0:
                ordered_list.insert(0, unordered_list[i])
                break

    # Return the ordered list
    return ordered_list

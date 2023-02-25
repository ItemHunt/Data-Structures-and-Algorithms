'''
Algorithms Module

Contents: Refer to README for a more detailed view

Sorting Algorithms
- Insertion Sort
- Selection Sort
- Bubble Sort
- Bucket Sort
'''

#Insertion Sort - O(n^2)
def insertion_sort(unordered_list):
    #Init
    ordered_list = [unordered_list[0]]

    #Inserition Sort Algorithm
    for i in range(1, len(unordered_list)): 
        #starts at index len(ordered_list) - 1, ends at -1, decrements per every loop
        for j in range(len(ordered_list) - 1, -1, -1):
            #Evaluates if the value at index j of the ordered list is less than the value at index i of the unordered list
            if ordered_list[j] < unordered_list[i]:
                ordered_list.insert(j + 1, unordered_list[i])
                break
            #if j is 0, it means that the value at index i of the unordered list is currently the smallest value
            elif j == 0:
                ordered_list.insert(0, unordered_list[i])
                break

    return ordered_list

#Selection Sort - O(n^2)
def selection_sort(lst):
    #Iterate thru the whole lst
    for i in range(0, len(lst)):
        #assign i to current index
        cur_idx = i

        #Iterate thru the whole lst except index i and below
        for j in range(i + 1, len(lst)):
            #If value at current index is greater than the value at index j
            #change current index to j
            if lst[cur_idx] > lst[j]:
                cur_idx = j
        #swap
        lst[i], lst[cur_idx] = lst[cur_idx], lst[i]

    return lst

#Bubble Sort - O(n^2)
def bubble_sort(lst):
    pass

def bucket_sort(lst):
    pass





                    

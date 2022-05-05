def quicksort(input_list, low, high):
    '''Function to perform in-place quick sort on a list of integers.

    Input: input_list, List[int]: a list of arbitrary integers.
            low, int: the starting index of the sublist to be sorted.
            high, int: the ending index of the sublist to be sorted.
    Output: List[int]: the sorted output of the input list.
    
    Quicksort is a divide-and-conquer sorting algorithm that selects a pivot, and then partitions the array into three
    parts around the pivot - elements smaller than pivot, equal to pivot, and larger than pivot. This implementation
    selects the pivot to always be the last element in the array, and executes quicksort recursively.
    
    The algorithm uses a partition() method to continually place the selected pivot into the correct position in the array,
    then bucket the elements smaller than it to its left, and the elements greater than it to its right.
     completes when the list is sorted, determined when all elements have been seen and inserted into the sub-list.

    Average-Case Complexity: O(nlogn) - ...
    Worst-Case Complexity: O(n^2) - occurs when the picked pivot is always an extreme (smallest of largest) value. In this case,
        because the picked pivot is always the last element, this happens when the array is already sorted/reverse sorted.
    '''
    #Base case - if low index crosses over high index, we know that the array up to that point is sorted, and we should return
    #**once a sublist is entirely sorted, recursive calls from that sublist return from scope by this condition
    if low < high:

        #partition the array based on a pivot element, where elements to its left are smaller & to its right are larger
        pivot_index = partition(input_list, low, high)

        #recursively call quicksort on the left sublist & then the right sublist
        #**the actual pivot is avoided as it is already in sorted location
        quicksort(input_list, low, pivot_index - 1)
        quicksort(input_list, pivot_index + 1, high)



def partition(input_list, low, high):
    '''Helper method to choose a pivot, slot the selected pivot into the correct position in the array, and place all elements smaller
    than the pivot to its left, and all elements larger than the pivot to its right in the array.

    Input: input_list, List[int]: a list of arbitrary integers.
            low, int: the starting index of the sublist to be sorted.
            high, int: the ending index of the sublist to be sorted.
    Output: int: the index of where the partition is completed; exactly the index of the sorted pivot.

    Partition moves elements smaller than the pivot element to the bottom of the array, and then finally slots the pivot
    into the correct location. This reduces the amount of operations performed by only operating on the smaller-than-pivot part
    of the sublist, yet still correctly buckets the list into its three parts.

    Input
    '''
    #select a pivot - let it always be the last element in the sublist
    pivot = input_list[high]

    #index of the currently smaller element; this is the correct location to which we should put the pivot so far.
    #**all smaller-than-pivot elements are placed contiguously into the leftmost part of the subarray
    i = low - 1 

    #traverse the sublist range to place the pivot correctly relative to other elements
    for j in range(low, high):
        if(input_list[j] <= pivot):

            #swap the j-index element with the greater element at index i, which places the j element into the 'smaller' bucket
            i = i + 1
            temp = input_list[i]
            input_list[i] = input_list[j]

            #place the smaller-than-pivot element in the leftmost position in subarray
            input_list[j] = temp

    #finally, swap the list's pivot with the greater element at index i, which places the pivot into final location
    temp = input_list[i + 1]
    input_list[i + 1] = input_list[high]    #the pivot's list index
    input_list[high] = temp

    #print("Low: " + str(low), " High: " + str(high), " Partitioned sublist: ", input_list)

    return i + 1
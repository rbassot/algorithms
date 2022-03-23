
def iter_binarysearch(sorted_list, value):
    '''Function to perform an iterative binary search for a specific element in a list.

    Input: sorted_list, List[int]: a list of sorted integers. Binary search can only  work on a sorted list.
           value, int: the value existing in the list that the search must find.
    Output: index, int: the index of input_list where the element was found. Returns -1 if the element doesn't exist.
    
    Binary search is a divide-and-conquer technique that compares partitions of the array to the value being searched
    for. This can be done because the array is sorted - therefore we can make assumptions about the rest of the values
    before and after a specific index, with respect to getting closer to/further from the target value. 

    Average-Case Complexity: O(log n) - Through divide and conquer on a sorted list, this algorithm partitions the
        list immediately and continues to divide the list in two, until the element is found.
    Worst-Case Complexity: O(log n)
    '''

    #set the bounds where the element can be found, which will be updated as the algorithm executes
    low = 0
    high = len(sorted_list) - 1

    while low <= high:

        #set the middlepoint to the median between the two bounds
        mid = low + (high - low) // 2

        #check the left partition; ignore it if the value isn't found there by adjusting the bound
        if sorted_list[mid] < value:
            low = mid + 1

        #check the right partition
        elif sorted_list[mid] > value:
            high = mid - 1

        #otherwise we know that mid is exactly the index where the value is found
        else:
            return mid

    return -1

def insertionsort(input_list):
    '''Function to perform insertion sort on a list of integers.

    Input: input_list, List[int]: a list of arbitrary integers.
    Output: List[int]: the sorted output of the input list.
    
    Insertionsort is a comparison-based sorting algorithm that keeps a sub-list of elements maintained (starting from the
    beginning of the array which is always sorted. An element gets directly inserted into the sublist by finding its exact
    location to be inserted into the sub-list. The algorithm completes when the list is sorted, determined when all
    elements have been seen and inserted into the sub-list.

    Average-Case Complexity: O(n^2) - The array is sequentially searched and the sub-list must be iterated through
        at each new element.
    Worst-Case Complexity: O(n^2)
    '''

    #iterate through the list from the start, and maintain a sorted sub-list of elements
    for i in range(len(input_list)):

        #select a value to be inserted into the sub-list
        j = i
        value = input_list[j]

        #shuffle sorted sub-list elements to the left until the value's correct slot is open 
        while j > 0 and input_list[j] > value:
            input_list[j] = input_list[j-1]
            j = j - 1

        #insert the value into the sorted location into the sub-list
        input_list[j] = value

    return input_list

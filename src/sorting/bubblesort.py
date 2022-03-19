
def swap_elements(xlist, i, j):
    '''Subroutine to swap two elements in a list, based on the indices passed. Returns the updated list.
    '''

    #swap elements in place
    temp = xlist[i]
    xlist[i] = xlist[j]
    xlist[j] = temp
    return xlist


def bubblesort(input_list):
    '''Function to perform bubble sort on a list of integers.

    Input: input_list, List[int]: a list of arbitrary integers.
    Output: List[int]: the sorted output of the input list.
    
    Bubblesort is a comparison-based sorting algorithm that compares pairs of adjacent elements. It starts at the first two
    list elements, and checks for adjacent inversions - any occurrence of an unsorted pair. If the pair is sorted, the algorithm
    continues to the next element. If the pair is not sorted (inverted), the algorithm swaps the indices in the array to fix the
    inversion, then continues to the next element. The algorithm completes when the list is sorted, determined when one entire
    iteration of the list contains no swap operations.

    Average-Case Complexity: O(n^2) - The outer loop iterates through the entire list, and the inner loop does the same.
    Worst-Case Complexity: O(n^2)
    '''

    #continually iterate through the list and track if a swap operation was performed
    for i in range(len(input_list)):
        swapped = False

        for j in range(len(input_list) - 1):

            #compare adjacent elements - swap them if they are inverted
            if(input_list[j] > input_list[j+1]):
                input_list = swap_elements(input_list, j, j+1)
                swapped = True

        #if no inversion was seen, the list is sorted
        if(not swapped):
            break

    return input_list
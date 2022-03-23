import sorting.bubblesort as bs
import sorting.insertionsort as ins
import searching.iter_binarysearch as i_bs

def main():

    #initialize a test list
    l = [1, 6, 8, -3, 12, 2, -8, 0, 17, 9, -20, 32]
    print("Initial test list: ", l)
    print()

    '''Sorting Algorithms'''
    #perform sorting operations, and print the sorted result
    sorted_list = bs.bubblesort(l)
    print("Bubblesort result: ", sorted_list)

    sorted_list = ins.insertionsort(l)
    print("Insertionsort result: ", sorted_list)


    '''Searching Algorithms'''
    #sort the list first, perform search, and print index
    print()
    l = [1, 6, 8, -3, 12, 2, -8, 0, 17, 9, -20, 32]
    l.sort()
    value = 12
    index = i_bs.iter_binarysearch(l, value)
    print("Iterative Binary Search index for target value " +  str(value) + ": " +  str(index),
         "; value at index: " +  str(sorted_list[index]))




if __name__ == "__main__":
    main()
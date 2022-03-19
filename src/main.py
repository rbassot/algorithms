import sorting.bubblesort as bs
import sorting.insertionsort as ins

def main():

    #initialize a test list
    l = [1, 6, 8, -3, 12, 2, -8, 0, 17, 9, -20, 32]
    print("Initial test list: ", l)
    print()

    #perform sorting operations, and print the sorted result
    sorted_list = bs.bubblesort(l)
    print("Bubblesort result: ", sorted_list)

    sorted_list = ins.insertionsort(l)
    print("Insertionsort result: ", sorted_list)
    


if __name__ == "__main__":
    main()
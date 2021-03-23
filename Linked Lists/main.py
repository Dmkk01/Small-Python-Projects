from linked_list import LinkedListException, LinkedList, Empty, Cell


def main():
    # This is a short example for creating and using the linked list.
    empty = Empty()
    cell_1 = Cell('abc', empty)
    cell_2 = Cell(56, cell_1)

    print(empty)
    print()
    print(cell_1)
    print()
    print(cell_2)
    print()
    print("Index: {}".format(cell_2.index('abc')))


if __name__ == "__main__":
    main()

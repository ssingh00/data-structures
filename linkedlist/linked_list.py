
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

if __name__ == '__main__':

    my_linked_list = LinkedList()
    my_linked_list.print_list()
#Empty

    my_linked_list.append(5)
    my_linked_list.append(2)
    my_linked_list.append(9)
    my_linked_list.print_list()
#5 2 9

    my_linked_list.prepend(4)
    my_linked_list.print_list()
#4 5 2 9

    my_linked_list.insert(2,7)
    my_linked_list.print_list()
#4 5 7 2 9

    my_linked_list.insert(0,0)
    my_linked_list.insert(6,0)
    my_linked_list.insert(9,3)
    my_linked_list.print_list()
#This position is not available. Inserting at the end of the list
#0 4 5 7 2 9 0 3

    my_linked_list.delete_by_value(3)
    my_linked_list.print_list()
#0 4 5 7 2 9 0

    my_linked_list.delete_by_value(0)
    my_linked_list.print_list()
#4 5 7 2 9 0

    my_linked_list.delete_by_position(3)
    my_linked_list.print_list()
#4 5 7 9 0

    my_linked_list.delete_by_position(0)
    my_linked_list.print_list()
#5 7 9 0

    my_linked_list.delete_by_position(8)
    my_linked_list.print_list()
#5 7 9
    print(my_linked_list.length)
#3
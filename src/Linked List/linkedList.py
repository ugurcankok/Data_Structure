class Node:
    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printing(self):
        if self.head is None:
            print("Linked list is empty!")
            return

        iteration = self.head
        linked_list_str = ""

        while iteration:
            linked_list_str += str(iteration.data) + ' --> ' if iteration.next else str(iteration.data)
            iteration = iteration.next

        print(linked_list_str)
    def insert_at_begining(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        node = Node(data, self.head)
        self.head = node



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(8)
    ll.printing()
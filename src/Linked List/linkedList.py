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

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_lists):
        self.head = None
        for data_list in data_lists:
            self.insert_at_end(data_list)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(8)
    ll.insert_at_end(6)
    ll.insert_values(["a","b","c","d"])
    print(f"Linked List Length: {ll.get_length()}" )
    ll.printing()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self) -> object:
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


llist = SingleLinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.prepend('D')
llist.print_list()

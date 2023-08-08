""" class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next


head = Node('Node 1')
head.next = Node('Node 2')
head.next.next = Node('Node 3')


iter_linked_list(head) """


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, value):
#         new_node = Node(value)

#         if self.head is None:
#             self.head = new_node
#             print('Head Node Created:', self.head.value)
#             return

#         node = self.head

#         while node.next is not None:
#             node = node.next

#         node.next = new_node
#         print('Appended new Node with value:', node.next.value)


# llist = LinkedList()
# llist.append('First Node')
# llist.append('Second Node')
# llist.append('Third Node')


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print('The head node is:', self.head.value)

        node = self.head
        while node.next is not None:
            node = node.next

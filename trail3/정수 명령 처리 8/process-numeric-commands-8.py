class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def push_back(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def pop_front(self):
        result = self.head.data

        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return result

    def pop_back(self):
        result = self.tail.data

        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return result


n = int(input())

ll = LinkedList()

for _ in range(n):
    command = input().split()

    if command[0] == "push_front":
        ll.push_front(int(command[1]))

    elif command[0] == "push_back":
        ll.push_back(int(command[1]))

    elif command[0] == "pop_front":
        print(ll.pop_front())

    elif command[0] == "pop_back":
        print(ll.pop_back())

    elif command[0] == "size":
        print(ll.size)

    elif command[0] == "empty":
        print(1 if ll.size == 0 else 0)

    elif command[0] == "front":
        print(ll.head.data)

    elif command[0] == "back":
        print(ll.tail.data)

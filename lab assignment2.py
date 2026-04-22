# dynamic array..............
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self.resize()

        self.data[self.size] = x
        self.size += 1

    def resize(self):
        print("Resizing from", self.capacity, "to", self.capacity * 2)
        self.capacity = self.capacity * 2
        new_array = [None] * self.capacity

        for i in range(self.size):
            new_array[i] = self.data[i]

        self.data = new_array

    def pop(self):
        if self.size == 0:
            return "Array empty"

        val = self.data[self.size - 1]
        self.size -= 1
        return val

    def display(self):
        print(self.data[:self.size])
        #...........single linked list............
        class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_end(self, x):
        new = Node(x)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new

    def delete_value(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        #............double linked list........
        class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new = DNode(x)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp

    def insert_after(self, target, x):
        temp = self.head

        while temp:
            if temp.data == target:
                new = DNode(x)
                new.next = temp.next
                new.prev = temp

                if temp.next:
                    temp.next.prev = new

                temp.next = new
                return
            temp = temp.next

    def delete_pos(self, pos):
        temp = self.head

        for i in range(pos):
            if temp is None:
                return
            temp = temp.next

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev
            #..............stack using linked list.....
            class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            return "Stack empty"

        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        if self.top:
            return self.top.data
        return "Empty"
    

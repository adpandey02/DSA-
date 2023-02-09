class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(node.value) for node in self.linkedlist]
        return '\n'.join(values)

    def isempty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
        
    def enqueue(self, value):
        newnode = Node(value)
        if self.isempty():
            self.linkedlist.head = newnode
            self.linkedlist.tail = newnode
        else:
            self.linkedlist.tail.next = newnode
            self.linkedlist.tail = newnode

    def dequeue(self):
        if self.isempty():
            return 'queue is empty'
        else:
            del_value = self.linkedlist.head.value
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return del_value

    def peek(self):
        if self.isempty():
            return 'queue is empty'
        else:
            return self.linkedlist.head.value

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None
        

custqueue = Queue()
custqueue.enqueue(1)
custqueue.enqueue(2)
custqueue.enqueue(3)
print(custqueue)
print(custqueue.peek())
print(custqueue)

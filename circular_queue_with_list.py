class Circularueue:
    def __init__(self, maxsize):
        self.start = -1
        self.end = -1
        self.list = maxsize * [None]
        self.maxsize = maxsize

    def __str__(self):
        value = [str(x) for x in self.list]
        return '\n'.join(value)

    def isfull(self):
        if self.start == 0 and self.end == self.maxsize - 1:
            return True
        elif self.end + 1 == self.start:
            return True
        else:
            return False

    def isempty(self):
        if self.end == -1:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.isfull():
            return 'queue is full'
        else:
            if self.start == -1:                        # for first element insertion only
                self.start = 0
            if self.end == self.maxsize - 1:
                self.end = 0
            else:
                self.end = self.end + 1
            self.list[self.end] = value
            return 'element inserted at the end of the queue'

    def dequeue(self):
        if self.isempty():
            return 'queue is empty'
        else:
            firstelement = self.list[self.start]
            start = self.start
            if self.start == self.maxsize-1:
                self.start = 0
            elif self.start == self.end:
                self.start = -1
                self.end = -1
            else:
                self.start += 1 
            self.list[start] = None
            return firstelement

    def peek(self):
        if self.isempty():
            return 'queue is empty'
        else:
            return self.list[self.start]

    def delete(self):
        self.list = self.maxsize * [None]
        self.end = -1
        self.start = -1







customqueue = Circularueue(maxsize=3)
print(customqueue.enqueue(1))
print(customqueue.enqueue(2))
print(customqueue.enqueue(3))
print(customqueue.isfull())
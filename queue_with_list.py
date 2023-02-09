
class Queue:

    def __init__(self):
        self.list = []
    
    def __str__(self):
        value = [str(i) for i in self.list]
        return '\n'.join(value)
    
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.list.append(value)
        return 'item added'

    def dequeue(self):
        if self.isempty():
            return 'queue is empty'
        else:
            del_value = self.list.pop(0)
            return f'first element {del_value} deleted'

    def peek(self):
        if self.isempty():
            return 'queue is empty'
        else:
            return self.list[0]
        
    def delete():
        self.list = None
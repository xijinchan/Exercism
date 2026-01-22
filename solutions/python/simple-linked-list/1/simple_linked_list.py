class Node:
    def __init__(self, value, next=None):
        self.value_ = value
        self.next_ = next

    def value(self):
        return self.value_

    def next(self):
        if next != None: return self.next_

class LinkedList:
    def __init__(self, values=[]):
        self.values = values
        self.head_ = None
        self.count = 0
        for i in values:
            self.push(i)

    def __len__(self):
        return self.count
            
    def __iter__(self):
        current_node = self.head_
        while current_node != None:
            yield current_node.value()
            current_node = current_node.next()

    def head(self):
        if self.head_ == None: raise EmptyListException('The list is empty.')
        return self.head_
    
    def push(self, value):
        self.head_ = Node(value, self.head_)
        self.count += 1

    def pop(self):
        if self.head_ == None: raise EmptyListException('The list is empty.')
        popped_value = self.head().value()
        self.count -= 1
        self.head_ = self.head().next()
        return popped_value

    def reversed(self):
        current_node = self.head_
        output = []
        for i in range(len(self)):
            output.append(current_node.value())
            current_node = current_node.next()
        output.reverse()
        return output

class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
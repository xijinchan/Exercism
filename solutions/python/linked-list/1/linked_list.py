class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value_ = value
        self.succeeding_ = succeeding
        self.previous_ = previous

    def value(self):
        return self.value_

    def succeeding(self):
        if self.succeeding_ != None: return self.succeeding_

    def previous(self):
        if self.previous_ != None: return self.previous_

class LinkedList:
    def __init__(self):
        self.head_ = None
        self.tail_ = None
        self.count = 0

    def __len__(self):
        return self.count

    def __iter__(self):
        current_node = self.head_
        while current_node != None:
            yield current_node.value()
            current_node = current_node.succeeding()

    def push(self, value):
        if self.head_ == None:
            self.head_ = Node(value, self.head_)
            self.tail_ = self.head_
            self.count +=1
        else:
            self.head_ = Node(value, self.head_)
            self.head().succeeding().previous_ = self.head_
            self.count +=1
    
    def head(self):
        return self.head_

    def tail(self):
        return self.tail_

    def pop(self):
        if self.count == 0: raise IndexError('List is empty')
        popped_value = self.head().value()
        self.head_ = self.head().succeeding()
        self.count -=1
        return popped_value

    def shift(self):
        if self.count == 0: raise IndexError('List is empty')
        shifted_value = self.tail().value()
        self.tail_ = self.tail().previous()
        if self.tail_ == None: self.head_ = None
        if self.tail() != None:
            if self.tail().succeeding_ != None:
                self.tail().succeeding_ = None # delete tail succeeding reference
        self.count -=1
        return shifted_value

    def unshift(self, value):
        if self.tail_ == None:
            self.tail_ = Node(value, None, self.tail_)
            self.head_ = self.tail_
        else:
            self.tail_ = Node(value, None, self.tail_)
            self.tail().previous().succeeding_ = self.tail_
        self.count +=1

    def delete(self, value):
        if self.count == 0: raise ValueError('List is empty')
        count = self.count
        current_node = self.head_
        for k in range(self.count):
            if current_node.value() == value:
                if k == 0:
                    self.pop()
                    break
                elif k == self.count-1:
                    self.shift()
                    break
                else:
                    current_node.succeeding().previous_ = current_node.previous()
                    current_node.previous().succeeding_ = current_node.succeeding()
                    self.count -= 1
                    break
            current_node = current_node.succeeding()
        if count == self.count: raise ValueError('Value not found')
                
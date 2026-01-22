class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * self.capacity
        self.order_write = [k for k in range(self.capacity)]
        self.order_read = [k for k in range(self.capacity)]

    def read(self):
        if self.buffer == [None] * self.capacity:
            raise BufferEmptyException('Circular buffer is empty')
        else:
            min_index = self.order_read.index(min(self.order_read))
            output = self.buffer[min_index]
            self.buffer[min_index] = None
            self.order_read = [k-1 for k in self.order_read]
            self.order_read[min_index] = self.capacity
            return output
    
    def write(self, data):
        if None not in self.buffer: raise BufferFullException('Circular buffer is full')
        min_index = self.order_write.index(min(self.order_write))
        self.buffer[min_index] = data
        self.order_write = [k-1 for k in self.order_write]
        self.order_write[min_index] = self.capacity

    def overwrite(self, data):
        min_index = self.order_write.index(min(self.order_write))
        self.buffer[min_index] = data
        self.order_write = [k-1 for k in self.order_write]
        self.order_write[min_index] = self.capacity
        self.order_read = [k-1 for k in self.order_read]
        self.order_read[min_index] = self.capacity
        
    def clear(self):
        self.buffer = [None] * self.capacity

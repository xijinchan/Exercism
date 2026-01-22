import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.read_calls = 0
        self.write_calls = 0
        self.bytes_written = 0
        self.bytes_read = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        return self

    def __next__(self):
        line = super().readline()
        if not line:
            raise StopIteration

        self.read_calls += 1
        self.bytes_read += len(line)
        return line

    def read(self, size=-1):
        total = super().read(size)

        self.read_calls += 1
        self.bytes_read += len(total)
        return total

    @property
    def read_bytes(self):
        return self.bytes_read

    @property
    def read_ops(self):
        return self.read_calls

    def write(self, b):
        total = super().write(b)

        self.write_calls += 1
        self.bytes_written += total
        return total

    @property
    def write_bytes(self):
        return self.bytes_written

    @property
    def write_ops(self):
        return self.write_calls


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self.socket_ = socket

        self.receive_calls = 0
        self.bytes_received = 0

        self.send_calls = 0
        self.bytes_sent = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.socket_.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        total = self.socket_.recv(bufsize, flags)
        self.receive_calls += 1
        self.bytes_received += len(total)
        return total

    @property
    def recv_bytes(self):
        return self.bytes_received

    @property
    def recv_ops(self):
        return self.receive_calls

    def send(self, data, flags=0):
        total = self.socket_.send(data, flags)
        
        self.send_calls += 1
        self.bytes_sent += total
        return total

    @property
    def send_bytes(self):
        return self.bytes_sent

    @property
    def send_ops(self):
        return self.send_calls

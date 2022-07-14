"""
#1 List based FIFO
Inserting and deleting from the beginning of the list takes O(n) time, which is not optimal.
"""


class Fifo1:
    def __init__(self):
        self.fifo = []

    def push(self, elem):
        self.fifo.append(elem)

    def pop(self):
        return self.fifo.pop(0)


"""
#2 collection.deque
Inserting and deleting elements from both ends in this case is O(1), 
since deque is based on a doubly linked list.
"""

from collections import deque


class Fifo2:
    def __init__(self):
        self.fifo = deque()

    def push(self, elem):
        self.fifo.append(elem)

    def pop(self):
        return self.fifo.popleft()


"""
#3 multiprocessing.Queue
This option is used for process-based parallel operation. 
"""

from multiprocessing import Queue


class Fifo3:
    def __init__(self):
        self.fifo = Queue()

    def push(self, elem):
        self.fifo.put(elem)

    def pop(self):
        return self.fifo.get()


"""
#4 queue.Queue
Fifo for multi-threaded use 
"""

from queue import Queue


class Fifo4:
    def __init__(self):
        self.fifo = Queue()

    def push(self, elem):
        self.fifo.put(elem)

    def pop(self):
        return self.fifo.get()
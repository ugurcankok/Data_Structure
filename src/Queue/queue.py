# First In First Out (FIFO)

# Using list as a queue

wmt_stock_price_queue = []

wmt_stock_price_queue.insert(0,131.10)
wmt_stock_price_queue.insert(0,132.12)
wmt_stock_price_queue.insert(0,135)

print(wmt_stock_price_queue)

wmt_stock_price_queue.pop()

wmt_stock_price_queue.pop()

print(wmt_stock_price_queue)

# Using collections.deque as a queue

from collections import deque
q = deque()

q.appendleft(5)
q.appendleft(8)
q.appendleft(10)

print(q)

q.pop()

q.pop()

# Implement queue class using collections.deque

from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.buffer)

print(pq.size())

pq.dequeue()

pq.dequeue()

print(pq.buffer)


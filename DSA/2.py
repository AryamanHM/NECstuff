class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# Test the Queue class
queue = Queue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

# Print the queue size
print("Queue size:", queue.size())

# Dequeue elements
print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())

# Print the queue size after dequeue
print("Queue size:", queue.size())

# Check if the queue is empty
print("Is the queue empty?", queue.is_empty())

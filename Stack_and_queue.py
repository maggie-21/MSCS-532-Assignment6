class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.data) == 0

    def display(self):
        return self.data


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.data[0]
        else:
            raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.data) == 0

    def display(self):
        return self.data


# Example usage
if __name__ == "__main__":
    # Stack Operations
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack.display())
    print("Peek top of stack:", stack.peek())
    print("Pop from stack:", stack.pop())
    print("Stack after pop:", stack.display())

    # Queue Operations
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueues:", queue.display())
    print("Peek front of queue:", queue.peek())
    print("Dequeue from queue:", queue.dequeue())
    print("Queue after dequeue:", queue.display())

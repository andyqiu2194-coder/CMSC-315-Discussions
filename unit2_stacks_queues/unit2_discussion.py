"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # A list stores the stack values, with the end of the list
        # representing the top of the stack.
        self.items = []

    def push(self, value):
        # Adding to the end allows the newest value to be removed first,
        # which demonstrates LIFO (Last-In, First-Out) behavior.
        self.items.append(value)

    def pop(self):
        # Remove and return the most recently added value.
        # Raise an error if the stack is empty.
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        # Peek returns the top value without removing it from the stack.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        return self.items[-1]

    def is_empty(self):
        # Return True when the stack contains no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # deque allows efficient additions at the back and removals
        # from the front of the queue.
        self.items = deque()

    def enqueue(self, value):
        # Adding to the back and removing from the front creates
        # FIFO (First-In, First-Out) behavior.
        self.items.append(value)

    def dequeue(self):
        # Remove and return the value at the front of the queue.
        # Raise an error if the queue is empty.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.popleft()

    def front(self):
        # Front returns the first value without removing it.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")
        return self.items[0]

    def is_empty(self):
        # Return True when the queue contains no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")

    # Create a Stack object.
    stack = Stack()

    # Add four values to demonstrate LIFO behavior.
    print("Adding 10, 20, 30, and 40 to the stack.")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    # The last value added is the first value removed.
    print("Stack uses LIFO: the last value added is removed first.")
    print("Top value:", stack.peek())

    print("Popping values from the stack:")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    # Demonstrate popping from an empty stack.
    print("\nTrying to pop from an empty stack:")
    try:
        stack.pop()
    except IndexError as error:
        print("Error:", error)

    # Demonstrate peeking at an empty stack.
    print("\nTrying to peek at an empty stack:")
    try:
        stack.peek()
    except IndexError as error:
        print("Error:", error)

    # Create a stack with one item.
    print("\nTesting a single-item stack:")
    single_stack = Stack()
    single_stack.push("Only item")
    print("Stack contains one item:", single_stack.peek())

    # Remove the only item.
    single_stack.pop()
    print("After removing the item, is the stack empty?",
          single_stack.is_empty())

    # ===============================
    # QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")

    # Create a Queue object.
    queue = Queue()

    # Add four values to demonstrate FIFO behavior.
    print("Adding 10, 20, 30, and 40 to the queue.")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    # The first value added is the first value removed.
    print("Queue uses FIFO: the first value added is removed first.")
    print("Front value:", queue.front())

    print("Dequeuing values from the queue:")
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    # Demonstrate dequeuing from an empty queue.
    print("\nTrying to dequeue from an empty queue:")
    try:
        queue.dequeue()
    except IndexError as error:
        print("Error:", error)

    # Demonstrate viewing the front of an empty queue.
    print("\nTrying to view the front of an empty queue:")
    try:
        queue.front()
    except IndexError as error:
        print("Error:", error)

    # Create a queue with one item.
    print("\nTesting a single-item queue:")
    single_queue = Queue()
    single_queue.enqueue("Only item")
    print("Queue contains one item:", single_queue.front())

    # Remove the only item.
    single_queue.dequeue()
    print("After removing the item, is the queue empty?",
          single_queue.is_empty())


if __name__ == "__main__":
    main()

class Queue:
    def __init__(self):
        self.queue = []

    # changed the name from "insert" to "enqueue" to better reflect the naming convention
    def enqueue(self, value):
        self.queue.append(value)

    # changed the name from "pop" to "dequeue" to better reflect the naming convention
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())


if __name__ == '__main__':
    main()
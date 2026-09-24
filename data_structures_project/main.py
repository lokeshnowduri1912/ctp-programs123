from data_structures import Stack, Queue


def show_account_data() -> None:
    stack: Stack[int] = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:", stack.items)
    print("Stack Peek:", stack.peek())
    print("Stack Pop:", stack.pop())
    print("Stack Size:", stack.size())

    queue: Queue[str] = Queue()

    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    print("\nQueue:", queue.items)
    print("Queue Front:", queue.front())
    print("Queue Dequeue:", queue.dequeue())
    print("Queue Size:", queue.size())


if __name__ == "__main__":
    show_account_data()
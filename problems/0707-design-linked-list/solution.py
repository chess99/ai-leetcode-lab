# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:31:59Z
# Experiment: ai-leetcode-lab, round 1
class _Node:
    def __init__(self, val: int = 0, next_node = None):
        self.val = val
        self.next = next_node


class MyLinkedList:

    def __init__(self):
        self.head = _Node()
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.head.next
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.tail.next = _Node(val)
        self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        previous = self.head
        for _ in range(index):
            previous = previous.next
        previous.next = _Node(val, previous.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        previous = self.head
        for _ in range(index):
            previous = previous.next
        if previous.next is self.tail:
            self.tail = previous
        previous.next = previous.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

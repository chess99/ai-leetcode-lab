# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:56:58Z
# Experiment: ai-leetcode-lab, round 1
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def _move(self) -> None:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self._move()
        return self.output.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._move()
        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.input and not self.output


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

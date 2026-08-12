# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:48Z
# Experiment: ai-leetcode-lab, round 1
class MyCalendarThree:

    def __init__(self):
        self.maximum = {}
        self.lazy = {}

    def book(self, startTime: int, endTime: int) -> int:
        def update(node, left, right):
            if startTime <= left and right < endTime:
                self.maximum[node] = self.maximum.get(node, 0) + 1
                self.lazy[node] = self.lazy.get(node, 0) + 1
                return
            middle = (left + right) // 2
            if startTime <= middle:
                update(node * 2, left, middle)
            if middle + 1 < endTime:
                update(node * 2 + 1, middle + 1, right)
            self.maximum[node] = self.lazy.get(node, 0) + max(
                self.maximum.get(node * 2, 0), self.maximum.get(node * 2 + 1, 0))

        update(1, 0, 10 ** 9)
        return self.maximum[1]


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)

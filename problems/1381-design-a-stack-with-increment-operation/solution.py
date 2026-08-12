# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:08Z
# Experiment: ai-leetcode-lab, round 1
class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.values = []
        self.pending_increment = []

    def push(self, x: int) -> None:
        if len(self.values) < self.max_size:
            self.values.append(x)
            self.pending_increment.append(0)

    def pop(self) -> int:
        if not self.values:
            return -1

        increment = self.pending_increment.pop()
        value = self.values.pop() + increment
        if self.pending_increment:
            self.pending_increment[-1] += increment
        return value

    def increment(self, k: int, val: int) -> None:
        if k > 0 and self.pending_increment:
            last_affected = min(k, len(self.pending_increment)) - 1
            self.pending_increment[last_affected] += val

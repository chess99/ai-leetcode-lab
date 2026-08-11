# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:45:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums); self.tree = [0] * (self.n + 1); self.nums = nums[:]
        for index, value in enumerate(nums): self._add(index + 1, value)

    def _add(self, index: int, delta: int) -> None:
        while index <= self.n: self.tree[index] += delta; index += index & -index

    def _sum(self, index: int) -> int:
        total = 0
        while index: total += self.tree[index]; index -= index & -index
        return total

    def update(self, index: int, val: int) -> None:
        self._add(index + 1, val - self.nums[index]); self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(right + 1) - self._sum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

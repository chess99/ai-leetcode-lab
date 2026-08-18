# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def sift_down(root: int, heap_size: int) -> None:
            while True:
                child = root * 2 + 1
                if child >= heap_size:
                    return
                right = child + 1
                if right < heap_size and nums[right] > nums[child]:
                    child = right
                if nums[root] >= nums[child]:
                    return
                nums[root], nums[child] = nums[child], nums[root]
                root = child

        for start in range(n // 2 - 1, -1, -1):
            sift_down(start, n)

        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            sift_down(0, end)

        return nums

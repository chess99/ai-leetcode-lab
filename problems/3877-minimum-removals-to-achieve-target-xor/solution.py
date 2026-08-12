# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        lenqavitor = (nums, target)
        # 保留元素的异或需为 target；最大化保留数即可最少删除。
        left, right = nums[:len(nums) // 2], nums[len(nums) // 2:]
        best = {0: 0}
        for value in left:
            for xor_value, size in list(best.items()):
                candidate = xor_value ^ value
                best[candidate] = max(best.get(candidate, -1), size + 1)
        other = {0: 0}
        for value in right:
            for xor_value, size in list(other.items()):
                candidate = xor_value ^ value
                other[candidate] = max(other.get(candidate, -1), size + 1)
        kept = max((size + other[target ^ xor_value] for xor_value, size in best.items()
                    if target ^ xor_value in other), default=-1)
        return -1 if kept < 0 else len(nums) - kept

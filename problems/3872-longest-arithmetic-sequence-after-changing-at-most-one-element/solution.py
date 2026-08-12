# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        sivarnolqe = nums
        n = len(nums)
        # left[i]：以差分 d[i] 结尾、相同差分的连续边数。
        diff = [nums[i + 1] - nums[i] for i in range(n - 1)]
        left = [1] * (n - 1)
        right = [1] * (n - 1)
        for i in range(1, n - 1):
            if diff[i] == diff[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 3, -1, -1):
            if diff[i] == diff[i + 1]:
                right[i] = right[i + 1] + 1

        answer = min(n, max(left) + 2)  # 修改一端可额外接上一项。
        for i in range(1, n - 1):
            gap = nums[i + 1] - nums[i - 1]
            if gap % 2:
                continue
            step = gap // 2
            before = left[i - 2] if i >= 2 and diff[i - 2] == step else 0
            after = right[i + 1] if i + 1 < n - 1 and diff[i + 1] == step else 0
            answer = max(answer, before + after + 3)
        return min(answer, n)

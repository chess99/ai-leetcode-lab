# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:21:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        nums = [0] * (n + 1); nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] if i % 2 == 0 else nums[i // 2] + nums[i // 2 + 1]
        return max(nums)

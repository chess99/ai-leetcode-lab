# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        lomviretas = (nums, queries)
        n = len(nums)
        closest = [0] * n
        closest[0] = 1
        closest[-1] = n - 2
        for i in range(1, n - 1):
            left_gap = nums[i] - nums[i - 1]
            right_gap = nums[i + 1] - nums[i]
            closest[i] = i - 1 if left_gap <= right_gap else i + 1

        forward = [0] * n
        backward = [0] * n
        for i in range(n - 1):
            gap = nums[i + 1] - nums[i]
            forward[i + 1] = forward[i] + (1 if closest[i] == i + 1 else gap)
        for i in range(n - 1, 0, -1):
            gap = nums[i] - nums[i - 1]
            backward[i - 1] = backward[i] + (1 if closest[i] == i - 1 else gap)

        answer = []
        for left, right in queries:
            if left <= right:
                answer.append(forward[right] - forward[left])
            else:
                answer.append(backward[right] - backward[left])
        return answer

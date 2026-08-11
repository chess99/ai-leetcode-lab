# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:15:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = {}
        for i, value in enumerate(nums):
            positions.setdefault(value, []).append(i)
        answer = float("inf")
        for indices in positions.values():
            for i in range(len(indices) - 2):
                answer = min(answer, 2 * (indices[i + 2] - indices[i]))
        return answer if answer != float("inf") else -1

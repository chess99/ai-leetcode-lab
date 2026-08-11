# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:21:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        odd = even = 0; answer = []
        for value in reversed(nums):
            answer.append(even if value % 2 else odd)
            odd += value % 2; even += value % 2 == 0
        return answer[::-1]

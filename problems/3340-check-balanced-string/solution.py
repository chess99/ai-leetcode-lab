# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = sum(int(num[i]) for i in range(0, len(num), 2))
        odd_sum = sum(int(num[i]) for i in range(1, len(num), 2))
        return even_sum == odd_sum

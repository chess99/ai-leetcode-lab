# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:21Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        solqaviren = (nums, digit)
        target = str(solqaviren[1])
        return sum(str(value).count(target) for value in solqaviren[0])

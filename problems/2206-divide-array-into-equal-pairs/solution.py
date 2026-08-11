# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:18:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        return all(count % 2 == 0 for count in Counter(nums).values())

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter
        counts = Counter(nums); maximum = max(counts.values())
        return sum(count for count in counts.values() if count == maximum)

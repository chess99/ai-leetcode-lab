# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:18:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        from collections import Counter
        return Counter(nums[i+1] for i in range(len(nums)-1) if nums[i] == key).most_common(1)[0][0]

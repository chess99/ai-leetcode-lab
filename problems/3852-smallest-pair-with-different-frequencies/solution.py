# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:18:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = {value: nums.count(value) for value in set(nums)}
        values = sorted(freq)
        for i, x in enumerate(values):
            for y in values[i + 1:]:
                if freq[x] != freq[y]: return [x, y]
        return [-1, -1]

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:28:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for index, number in enumerate(nums):
            if number in last_seen and index - last_seen[number] <= k:
                return True
            last_seen[number] = index
        return False

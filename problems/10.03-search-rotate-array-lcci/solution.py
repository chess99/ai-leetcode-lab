# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        for index, value in enumerate(arr):
            if value == target:
                return index
        return -1

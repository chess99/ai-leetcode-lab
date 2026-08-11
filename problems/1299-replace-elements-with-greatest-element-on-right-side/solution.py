# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:38:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], greatest = greatest, max(greatest, arr[i])
        return arr

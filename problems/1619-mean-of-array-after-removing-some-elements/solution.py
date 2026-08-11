# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:33:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        cut = len(arr) // 20
        return sum(arr[cut:-cut]) / (len(arr) - 2 * cut)

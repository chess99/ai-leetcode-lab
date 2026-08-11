# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:05:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return all(arr[i] - arr[i-1] == arr[1] - arr[0] for i in range(2, len(arr)))

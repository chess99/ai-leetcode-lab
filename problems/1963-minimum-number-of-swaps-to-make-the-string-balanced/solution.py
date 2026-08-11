# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance=maximum=0
        for char in s:
            imbalance += 1 if char=='[' else -1
            maximum=max(maximum,-imbalance)
        return (maximum+1)//2

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:28:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward = {}
        backward = {}
        for left, right in zip(s, t):
            if forward.get(left, right) != right or backward.get(right, left) != left:
                return False
            forward[left] = right
            backward[right] = left
        return True

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:56:21Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1: return '0'
        middle = 1 << (n - 1)
        if k == middle: return '1'
        if k < middle: return self.findKthBit(n - 1, k)
        return '1' if self.findKthBit(n - 1, (1 << n) - k) == '0' else '0'

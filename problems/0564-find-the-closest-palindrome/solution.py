# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n); value = int(n); prefix = int(n[:(length + 1) // 2])
        candidates = {10 ** (length - 1) - 1, 10 ** length + 1}
        for p in (prefix - 1, prefix, prefix + 1):
            text = str(p); candidates.add(int(text + (text[::-1] if length % 2 == 0 else text[-2::-1])))
        candidates.discard(value)
        return str(min(candidates, key=lambda x: (abs(x - value), x)))

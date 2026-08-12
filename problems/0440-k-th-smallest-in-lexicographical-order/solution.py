# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1
        while k:
            first, following, steps = current, current + 1, 0
            while first <= n:
                steps += min(n + 1, following) - first
                first *= 10
                following *= 10
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1
        return current

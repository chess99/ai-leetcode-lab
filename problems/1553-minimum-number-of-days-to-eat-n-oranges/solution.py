# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:10:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minDays(self, n: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def f(x):return x if x <= 1 else 1+min(x%2+f(x//2),x%3+f(x//3))
        return f(n)

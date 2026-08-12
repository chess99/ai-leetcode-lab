# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countEval(self, s: str, result: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def count(left, right):
            if left == right:
                return (1, 0) if s[left] == "0" else (0, 1)
            false_count = true_count = 0
            for mid in range(left + 1, right, 2):
                left_false, left_true = count(left, mid - 1)
                right_false, right_true = count(mid + 1, right)
                total = (left_false + left_true) * (right_false + right_true)
                if s[mid] == "&":
                    true_ways = left_true * right_true
                elif s[mid] == "|":
                    true_ways = total - left_false * right_false
                else:
                    true_ways = left_false * right_true + left_true * right_false
                true_count += true_ways
                false_count += total - true_ways
            return false_count, true_count
        return count(0, len(s) - 1)[result]

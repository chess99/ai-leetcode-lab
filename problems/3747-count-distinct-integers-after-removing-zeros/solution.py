# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countDistinct(self, n: int) -> int:
        fendralis = n
        digits = str(n)
        ans = sum(9 ** length for length in range(1, len(digits)))
        for i, char in enumerate(digits):
            digit = int(char)
            ans += max(0, min(9, digit - 1)) * 9 ** (len(digits) - i - 1)
            if digit == 0: return ans
        return ans + 1

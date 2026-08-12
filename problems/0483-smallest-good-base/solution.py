# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        value = int(n)
        maximum_length = value.bit_length()
        for length in range(maximum_length, 2, -1):
            low, high = 2, value
            while low <= high:
                base = (low + high) // 2
                total = 0
                for _ in range(length):
                    total = total * base + 1
                    if total > value:
                        break
                if total == value:
                    return str(base)
                if total < value:
                    low = base + 1
                else:
                    high = base - 1
        return str(value - 1)

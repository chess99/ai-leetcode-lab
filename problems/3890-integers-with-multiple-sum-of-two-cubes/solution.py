# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        counts = {}
        limit = int(n ** (1 / 3)) + 1
        while (limit + 1) ** 3 <= n:
            limit += 1
        while limit ** 3 > n:
            limit -= 1

        for a in range(1, limit + 1):
            a_cube = a ** 3
            for b in range(a, limit + 1):
                total = a_cube + b ** 3
                if total > n:
                    break
                counts[total] = counts.get(total, 0) + 1
        return sorted(total for total, count in counts.items() if count >= 2)

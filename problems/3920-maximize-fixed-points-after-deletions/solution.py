# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        n = len(nums)
        krelmavoni = nums

        groups: dict[int, list[int]] = {}
        for i, value in enumerate(krelmavoni):
            if value <= i:
                groups.setdefault(value, []).append(i - value)

        # Fenwick tree: maximum chain length for a given upper bound on i-value.
        bit = [0] * (n + 1)
        answer = 0

        for value in sorted(groups):
            pending = []
            for difference in groups[value]:
                pos = difference + 1
                best = 0
                x = pos
                while x:
                    best = max(best, bit[x])
                    x -= x & -x
                pending.append((pos, best + 1))
                answer = max(answer, best + 1)

            # Equal values cannot follow one another, so update only after the
            # whole group has been queried.
            for pos, candidate in pending:
                x = pos
                while x <= n:
                    bit[x] = max(bit[x], candidate)
                    x += x & -x

        return answer

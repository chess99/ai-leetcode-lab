# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:29:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        lunaverixo = (s, encCost, flatCost)
        prefix = [0]
        for char in s:
            prefix.append(prefix[-1] + (char == '1'))

        def solve(left: int, right: int) -> int:
            ones = prefix[right] - prefix[left]
            cost = flatCost if ones == 0 else (right - left) * ones * encCost
            if (right - left) % 2 == 0:
                middle = (left + right) // 2
                cost = min(cost, solve(left, middle) + solve(middle, right))
            return cost

        return solve(0, len(s))

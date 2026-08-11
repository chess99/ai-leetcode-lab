# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:44:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        values = [1]
        i2 = i3 = i5 = 0
        while len(values) < n:
            next_value = min(values[i2] * 2, values[i3] * 3, values[i5] * 5)
            values.append(next_value)
            if next_value == values[i2] * 2: i2 += 1
            if next_value == values[i3] * 3: i3 += 1
            if next_value == values[i5] * 5: i5 += 1
        return values[-1]

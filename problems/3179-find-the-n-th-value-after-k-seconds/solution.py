# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        modulo = 10**9 + 7
        values = [1] * n
        for _ in range(k):
            for index in range(1, n):
                values[index] = (values[index] + values[index - 1]) % modulo
        return values[-1]

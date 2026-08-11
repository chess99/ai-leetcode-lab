# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        modulo = 10**9 + 7
        learned = [0] * (n + 1)
        learned[1] = 1
        sharing = 0

        for day in range(2, n + 1):
            if day - delay >= 1:
                sharing += learned[day - delay]
            if day - forget >= 1:
                sharing -= learned[day - forget]

            sharing %= modulo
            learned[day] = sharing

        first_aware_day = max(1, n - forget + 1)
        return sum(learned[first_aware_day:]) % modulo

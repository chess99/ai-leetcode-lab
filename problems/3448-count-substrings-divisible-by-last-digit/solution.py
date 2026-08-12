# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countSubstrings(self, s: str) -> int:
        counts = [None] + [[0] * divisor for divisor in range(1, 10)]
        answer = 0
        for character in s:
            digit = int(character)
            for divisor in range(1, 10):
                new = [0] * divisor
                new[digit % divisor] += 1
                for remainder, amount in enumerate(counts[divisor]):
                    new[(remainder * 10 + digit) % divisor] += amount
                counts[divisor] = new
            if digit:
                answer += counts[digit][0]
        return answer

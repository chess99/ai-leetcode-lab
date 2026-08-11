# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        digit = str(x)
        if n[0] == "-":
            for index in range(1, len(n)):
                if n[index] > digit:
                    return n[:index] + digit + n[index:]
            return n + digit

        for index, character in enumerate(n):
            if character < digit:
                return n[:index] + digit + n[index:]
        return n + digit

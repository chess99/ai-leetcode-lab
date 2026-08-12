# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        suffix = int(s)

        def f(x):
            if x < suffix:
                return 0
            upper = (x - suffix) // (10 ** len(s))
            digits = str(upper)
            answer = 0
            for index, character in enumerate(digits):
                digit = int(character)
                answer += min(digit, limit + 1) * (limit + 1) ** (len(digits) - index - 1)
                if digit > limit:
                    return answer
            return answer + 1
        return f(finish)-f(start-1)

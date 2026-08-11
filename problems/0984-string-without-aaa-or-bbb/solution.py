# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        while a or b:
            if len(result) >= 2 and result[-1] == result[-2]:
                character = "b" if result[-1] == "a" else "a"
            else:
                character = "a" if a >= b else "b"
            result.append(character)
            if character == "a":
                a -= 1
            else:
                b -= 1
        return "".join(result)

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countHomogenous(self, s: str) -> int:
        modulo = 1_000_000_007
        total = 0
        run_length = 0
        previous = ""

        for character in s:
            if character == previous:
                run_length += 1
            else:
                previous = character
                run_length = 1
            total += run_length

        return total % modulo

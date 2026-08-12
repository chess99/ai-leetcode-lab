# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def crackNumber(self, ciphertext: int) -> int:
        text = str(ciphertext)
        previous_two = previous_one = 1
        for index in range(1, len(text)):
            current = previous_one
            if '10' <= text[index - 1:index + 1] <= '25':
                current += previous_two
            previous_two, previous_one = previous_one, current
        return previous_one

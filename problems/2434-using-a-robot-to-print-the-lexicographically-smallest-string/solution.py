# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def robotWithString(self, s: str) -> str:
        suffix_minimum = ["{"] * (len(s) + 1)

        for index in range(len(s) - 1, -1, -1):
            suffix_minimum[index] = min(s[index], suffix_minimum[index + 1])

        stack = []
        output = []

        for index, char in enumerate(s):
            stack.append(char)
            while stack and stack[-1] <= suffix_minimum[index + 1]:
                output.append(stack.pop())

        return "".join(output)

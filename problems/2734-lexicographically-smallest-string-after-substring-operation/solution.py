# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestString(self, s: str) -> str:
        chars = list(s)
        index = 0
        while index < len(chars) and chars[index] == "a":
            index += 1
        if index == len(chars):
            chars[-1] = "z"
        else:
            while index < len(chars) and chars[index] != "a":
                chars[index] = chr(ord(chars[index]) - 1)
                index += 1
        return "".join(chars)

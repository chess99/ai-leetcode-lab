# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:47:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getSmallestString(self, s: str) -> str:
        chars = list(s)
        for index in range(len(chars) - 1):
            if chars[index] > chars[index + 1] and (ord(chars[index]) - ord(chars[index + 1])) % 2 == 0:
                chars[index], chars[index + 1] = chars[index + 1], chars[index]
                break
        return "".join(chars)

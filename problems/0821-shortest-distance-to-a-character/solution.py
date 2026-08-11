# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:05:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = [len(s)] * len(s)
        previous = -len(s)
        for index, char in enumerate(s):
            if char == c:
                previous = index
            result[index] = index - previous
        previous = 2 * len(s)
        for index in range(len(s) - 1, -1, -1):
            if s[index] == c:
                previous = index
            result[index] = min(result[index], previous - index)
        return result

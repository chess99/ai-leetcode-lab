# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:10:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestAwesome(self, s: str) -> int:
        first = {0: -1}; mask = answer = 0
        for index, char in enumerate(s):
            mask ^= 1 << int(char)
            first.setdefault(mask, index)
            answer = max(answer, index - first[mask])
            for bit in range(10):
                if mask ^ (1 << bit) in first: answer = max(answer, index - first[mask ^ (1 << bit)])
        return answer

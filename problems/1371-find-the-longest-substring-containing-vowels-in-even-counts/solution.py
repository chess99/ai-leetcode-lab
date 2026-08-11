# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bits = {'a':1,'e':2,'i':4,'o':8,'u':16}
        first = {0:-1}; mask = answer = 0
        for index, char in enumerate(s):
            mask ^= bits.get(char, 0)
            if mask in first: answer = max(answer, index - first[mask])
            else: first[mask] = index
        return answer

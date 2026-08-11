# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        answer = 0
        for character in set(s):
            left, right = s.index(character), s.rindex(character)
            answer += len(set(s[left + 1:right]))
        return answer

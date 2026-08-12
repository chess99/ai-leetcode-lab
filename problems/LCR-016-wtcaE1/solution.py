# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = answer = 0
        for right, char in enumerate(s):
            left = max(left, last.get(char, -1) + 1)
            last[char] = right
            answer = max(answer, right - left + 1)
        return answer

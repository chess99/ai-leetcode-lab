# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        answer = 0
        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            while count[char] > 2:
                removed = s[left]
                count[removed] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer

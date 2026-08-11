# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        left = ''.join(chr(i + ord('a')) * (count[i] // 2) for i in range(26))
        middle = next((chr(i + ord('a')) for i in range(26) if count[i] % 2), '')
        return left + middle + left[::-1]

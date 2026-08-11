# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        characters = list(palindrome)
        for index in range(len(characters) // 2):
            if characters[index] != "a":
                characters[index] = "a"
                return "".join(characters)
        characters[-1] = "b"
        return "".join(characters)

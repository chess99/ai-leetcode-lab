# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        i = ans = 0
        while i + 1 < len(word):
            if abs(ord(word[i]) - ord(word[i + 1])) <= 1:
                ans += 1; i += 2
            else:
                i += 1
        return ans

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        ans = 0
        vowels = set('aeiou')
        for i in range(len(s)):
            count = 0
            for j in range(i, len(s)):
                count += 1 if s[j] in vowels else -1
                length = j - i + 1
                if count == 0 and (length // 2) ** 2 % k == 0:
                    ans += 1
        return ans

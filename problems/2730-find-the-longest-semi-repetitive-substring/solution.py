# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = pairs = answer = 0
        for right in range(len(s)):
            if right > 0 and s[right] == s[right - 1]:
                pairs += 1
            while pairs > 1:
                if s[left] == s[left + 1]:
                    pairs -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer

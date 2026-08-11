# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:00:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        previous = answer = 0
        current = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                answer += min(previous, current)
                previous, current = current, 1
        return answer + min(previous, current)

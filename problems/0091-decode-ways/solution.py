# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:17:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0] == "0":
            return 0
        previous, current = 1, 1
        for index in range(1, len(s)):
            next_count = current if s[index] != "0" else 0
            if "10" <= s[index - 1:index + 1] <= "26":
                next_count += previous
            previous, current = current, next_count
        return current

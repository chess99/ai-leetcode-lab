# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:02:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        run_length = 1
        for index in range(1, len(s) + 1):
            if index < len(s) and s[index] == s[index - 1]:
                run_length += 1
            else:
                if run_length == k:
                    return True
                run_length = 1
        return False

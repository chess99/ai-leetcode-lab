# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:48:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        answer = 0
        for left in range(len(s)):
            zero_count = one_count = 0
            for right in range(left, len(s)):
                if s[right] == "0":
                    zero_count += 1
                else:
                    one_count += 1
                if zero_count <= k or one_count <= k:
                    answer += 1
        return answer

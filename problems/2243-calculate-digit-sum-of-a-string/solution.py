# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:24:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = ''.join(str(sum(map(int, s[index:index + k]))) for index in range(0, len(s), k))
        return s

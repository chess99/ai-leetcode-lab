# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:45:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for start in range(0, len(chars), 2 * k):
            chars[start:start + k] = reversed(chars[start:start + k])
        return "".join(chars)

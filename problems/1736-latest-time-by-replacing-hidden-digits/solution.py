# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:31:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumTime(self, time: str) -> str:
        chars = list(time)
        if chars[0] == '?':
            chars[0] = '2' if chars[1] == '?' or chars[1] <= '3' else '1'
        if chars[1] == '?':
            chars[1] = '3' if chars[0] == '2' else '9'
        if chars[3] == '?':
            chars[3] = '5'
        if chars[4] == '?':
            chars[4] = '9'
        return ''.join(chars)

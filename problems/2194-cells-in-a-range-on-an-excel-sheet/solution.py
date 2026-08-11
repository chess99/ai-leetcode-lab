# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:18:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [chr(column) + str(row) for column in range(ord(s[0]), ord(s[3]) + 1) for row in range(int(s[1]), int(s[4]) + 1)]

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:04:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f'{n:,}'.replace(',','.')

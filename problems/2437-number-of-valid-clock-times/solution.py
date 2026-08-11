# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countTime(self, time: str) -> int:
        hours, minutes = time.split(':')
        return sum(f'{h:02d}'.startswith(hours) for h in range(24)) * sum(f'{m:02d}'.startswith(minutes) for m in range(60))

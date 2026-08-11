# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:52:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def lastRemaining(self, n: int) -> int:
        head=1; step=1; left=True; remaining=n
        while remaining>1:
            if left or remaining%2: head+=step
            remaining//=2; step*=2; left=not left
        return head

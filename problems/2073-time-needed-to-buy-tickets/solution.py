# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(value,tickets[k] if i<=k else tickets[k]-1) for i,value in enumerate(tickets))

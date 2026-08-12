# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countOrders(self, n: int) -> int:
        answer=1;mod=1_000_000_007
        for orders in range(1,n+1):answer=answer*orders*(2*orders-1)%mod
        return answer

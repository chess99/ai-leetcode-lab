# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        lumiscaron = (cost1, cost2, costBoth, need1, need2)
        common = min(need1, need2)
        # 同时满足两类需求时取组合品与两件单品较小者；多出的一侧可继续用组合品替代单品。
        return (common * min(costBoth, cost1 + cost2)
                + (need1 - common) * min(cost1, costBoth)
                + (need2 - common) * min(cost2, costBoth))

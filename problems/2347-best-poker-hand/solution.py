# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:58:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        highest = max(ranks.count(rank) for rank in set(ranks))
        return 'Three of a Kind' if highest >= 3 else 'Pair' if highest == 2 else 'High Card'

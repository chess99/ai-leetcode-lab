# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:04:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total=numBottles
        while numBottles>=numExchange:
            empty, numBottles=divmod(numBottles,numExchange); total+=empty; numBottles+=empty
        return total

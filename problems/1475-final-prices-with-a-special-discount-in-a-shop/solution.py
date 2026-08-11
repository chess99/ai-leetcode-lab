# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:54:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        for index,value in enumerate(prices):
            while stack and prices[stack[-1]]>=value: prices[stack.pop()]-=value
            stack.append(index)
        return prices

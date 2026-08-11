# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def possible(amount):
            for recipe in composition:
                spend=sum(max(0,need*amount-have)*price for need,have,price in zip(recipe,stock,cost))
                if spend<=budget: return True
            return False
        lo,hi=0,10**9
        while lo<hi:
            mid=(lo+hi+1)//2
            if possible(mid): lo=mid
            else: hi=mid-1
        return lo

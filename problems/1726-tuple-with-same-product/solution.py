# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:24Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products=Counter(nums[i]*nums[j] for i in range(len(nums)) for j in range(i))
        return sum(count*(count-1)*4 for count in products.values())

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(squares, values):
            total=0
            for number in squares:
                seen={}; target=number*number
                for value in values:
                    if target%value==0: total+=seen.get(target//value,0)
                    seen[value]=seen.get(value,0)+1
            return total
        return count(nums1,nums2)+count(nums2,nums1)

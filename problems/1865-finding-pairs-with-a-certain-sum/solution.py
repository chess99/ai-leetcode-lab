# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:36Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1;self.nums2=nums2;self.counts=Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.counts[self.nums2[index]]-=1;self.nums2[index]+=val;self.counts[self.nums2[index]]+=1

    def count(self, tot: int) -> int:
        return sum(self.counts[tot-value] for value in self.nums1)


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:06:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:return nums1[i]
            if nums1[i]<nums2[j]:i+=1
            else:j+=1
        return -1

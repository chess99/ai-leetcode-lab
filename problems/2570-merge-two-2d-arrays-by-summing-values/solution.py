# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:08:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        values={}
        for key,value in nums1+nums2:values[key]=values.get(key,0)+value
        return [[key,values[key]] for key in sorted(values)]

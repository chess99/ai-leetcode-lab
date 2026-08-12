# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        st=[];n=len(nums)
        for i in range(n+1):
            x=nums[i] if i<n else 0
            while st and nums[st[-1]]>x:
                j=st.pop();length=i-(st[-1] if st else -1)-1
                if nums[j]*length>threshold:return length
            st.append(i)
        return -1

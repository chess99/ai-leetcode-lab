# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        import heapq
        heap=[(row[0],i,0)for i,row in enumerate(nums)];heapq.heapify(heap);high=max(x[0]for x in nums);best=[heap[0][0],high]
        while True:
            low,i,j=heapq.heappop(heap)
            if high-low<best[1]-best[0]:best=[low,high]
            if j+1==len(nums[i]):return best
            value=nums[i][j+1];high=max(high,value);heapq.heappush(heap,(value,i,j+1))

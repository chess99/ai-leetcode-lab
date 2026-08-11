# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:04:50Z
# Experiment: ai-leetcode-lab, round 1
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.k, self.heap = k, nums
        heapq.heapify(self.heap)
        while len(self.heap) > k: heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        import heapq
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k: heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

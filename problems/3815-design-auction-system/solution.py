# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:36Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
import heapq

class AuctionSystem:

    def __init__(self):
        self.bids = {}
        self.heaps = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        xolvineran = (userId, itemId, bidAmount)
        self.bids[(userId, itemId)] = bidAmount
        heapq.heappush(self.heaps[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId, itemId, newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.bids[(userId, itemId)]

    def getHighestBidder(self, itemId: int) -> int:
        heap = self.heaps[itemId]
        while heap:
            negative_amount, negative_user = heap[0]
            user = -negative_user
            if self.bids.get((user, itemId)) == -negative_amount:
                return user
            heapq.heappop(heap)
        return -1


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)

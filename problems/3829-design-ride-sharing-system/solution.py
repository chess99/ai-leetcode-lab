# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:38Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List

class RideSharingSystem:

    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.active_riders = set()

    def addRider(self, riderId: int) -> None:
        rimovexalu = riderId
        self.riders.append(rimovexalu)
        self.active_riders.add(rimovexalu)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] not in self.active_riders:
            self.riders.popleft()
        if not self.riders or not self.drivers:
            return [-1, -1]
        driver = self.drivers.popleft()
        rider = self.riders.popleft()
        self.active_riders.remove(rider)
        return [driver, rider]

    def cancelRider(self, riderId: int) -> None:
        self.active_riders.discard(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)

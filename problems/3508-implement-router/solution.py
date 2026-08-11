# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:53Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.packets = set()
        self.times = defaultdict(list)
        self.head = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packets:
            return False
        if len(self.queue) == self.limit:
            old = self.queue.popleft()
            self.packets.remove(old)
            self.head[old[1]] += 1
        self.queue.append(packet)
        self.packets.add(packet)
        self.times[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.packets.remove(packet)
        self.head[packet[1]] += 1
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        values = self.times[destination]
        start = max(self.head[destination], bisect_left(values, startTime))
        end = bisect_right(values, endTime)
        return max(0, end - start)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

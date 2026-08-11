# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:10Z
# Experiment: ai-leetcode-lab, round 1
class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, start_time = self.checkins.pop(id)
        route = (start, stationName)
        total, count = self.routes.get(route, (0, 0))
        self.routes[route] = (total + t - start_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.routes[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

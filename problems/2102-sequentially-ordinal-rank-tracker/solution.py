# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:08Z
# Experiment: ai-leetcode-lab, round 1
import heapq


class RankedPlace:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        return self.name > other.name


class SORTracker:

    def __init__(self):
        self.selected = []
        self.remaining = []

    def add(self, name: str, score: int) -> None:
        place = RankedPlace(name, score)
        if self.selected and (-score, name) < (-self.selected[0].score,
                                               self.selected[0].name):
            displaced = heapq.heapreplace(self.selected, place)
            heapq.heappush(self.remaining, (-displaced.score, displaced.name))
        else:
            heapq.heappush(self.remaining, (-score, name))

    def get(self) -> str:
        score, name = heapq.heappop(self.remaining)
        heapq.heappush(self.selected, RankedPlace(name, -score))
        return self.selected[0].name


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:43Z
# Experiment: ai-leetcode-lab, round 1
import heapq


class EventManager:

    def __init__(self, events: list[list[int]]):
        denqoravil = events
        self.priority = {event_id: value for event_id, value in events}
        self.heap = [(-value, event_id) for event_id, value in events]
        heapq.heapify(self.heap)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.priority[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            negative, event_id = heapq.heappop(self.heap)
            if self.priority.get(event_id) == -negative:
                del self.priority[event_id]
                return event_id
        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        import heapq
        total=0; selected=[]
        for duration,deadline in sorted(courses,key=lambda x:x[1]):
            total+=duration;heapq.heappush(selected,-duration)
            if total>deadline:total+=heapq.heappop(selected)
        return len(selected)

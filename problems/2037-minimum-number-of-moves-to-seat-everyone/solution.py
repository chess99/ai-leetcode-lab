# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(seat - student) for seat, student in zip(sorted(seats), sorted(students)))

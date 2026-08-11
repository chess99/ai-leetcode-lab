# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:24:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [students.count(0), students.count(1)]
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                return sum(counts)
            counts[sandwich] -= 1
        return 0

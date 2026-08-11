# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive, negative = set(positive_feedback), set(negative_feedback)
        ranks = []
        for text, sid in zip(report, student_id):
            score = sum(3 if word in positive else -1 if word in negative else 0 for word in text.split())
            ranks.append((-score, sid))
        ranks.sort()
        return [sid for _, sid in ranks[:k]]

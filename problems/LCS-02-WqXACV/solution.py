# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:52:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        frequencies = {}
        for question in questions:
            frequencies[question] = frequencies.get(question, 0) + 1
        remaining = len(questions) // 2
        types = 0
        for count in sorted(frequencies.values(), reverse=True):
            remaining -= count
            types += 1
            if remaining <= 0:
                return types

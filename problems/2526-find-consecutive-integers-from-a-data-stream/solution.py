# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.streak = 0

    def consec(self, num: int) -> bool:
        self.streak = self.streak + 1 if num == self.value else 0
        return self.streak >= self.k

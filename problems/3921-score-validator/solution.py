# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:21:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = counter = 0
        for event in events:
            if event == "W": counter += 1
            else: score += 1 if event in ("WD", "NB") else int(event)
            if counter == 10: break
        return [score, counter]

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-13
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, _, content = log.partition(" ")
            if content[-1].isalpha():
                letter_logs.append((content, identifier, log))
            else:
                digit_logs.append(log)

        letter_logs.sort(key=lambda entry: (entry[0], entry[1]))
        return [entry[2] for entry in letter_logs] + digit_logs

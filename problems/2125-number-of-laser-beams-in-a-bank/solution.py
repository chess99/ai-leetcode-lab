# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        previous_devices = 0

        for row in bank:
            current_devices = row.count("1")
            if current_devices == 0:
                continue

            beams += previous_devices * current_devices
            previous_devices = current_devices

        return beams

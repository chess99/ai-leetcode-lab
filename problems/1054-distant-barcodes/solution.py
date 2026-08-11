# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:14:38Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        result = [0] * len(barcodes)
        index = 0
        for barcode, count in Counter(barcodes).most_common():
            for _ in range(count):
                result[index] = barcode
                index += 2
                if index >= len(barcodes):
                    index = 1
        return result

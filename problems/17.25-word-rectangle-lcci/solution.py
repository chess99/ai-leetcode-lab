# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:32Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        by_length = defaultdict(list)
        word_sets = defaultdict(set)
        prefixes = defaultdict(set)
        for word in words:
            by_length[len(word)].append(word)
            word_sets[len(word)].add(word)
            for end in range(len(word) + 1):
                prefixes[len(word)].add(word[:end])

        dimensions = sorted(
            ((width * height, width, height) for width in by_length for height in by_length),
            reverse=True,
        )
        for _, width, height in dimensions:
            rectangle = []

            def search() -> bool:
                row_count = len(rectangle)
                column_prefixes = ["".join(row[column] for row in rectangle) for column in range(width)]
                if row_count == height:
                    return all(prefix in word_sets[height] for prefix in column_prefixes)
                if any(prefix not in prefixes[height] for prefix in column_prefixes):
                    return False
                for word in by_length[width]:
                    if all(column_prefixes[column] + word[column] in prefixes[height] for column in range(width)):
                        rectangle.append(word)
                        if search():
                            return True
                        rectangle.pop()
                return False

            if search():
                return rectangle
        return []

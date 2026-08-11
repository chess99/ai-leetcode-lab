# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:29:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result = []
        for path in sorted(folder):
            if not result or not path.startswith(result[-1] + "/"):
                result.append(path)
        return result

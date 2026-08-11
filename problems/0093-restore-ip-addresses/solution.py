# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:18:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(start: int, parts: List[str]) -> None:
            remaining_parts = 4 - len(parts)
            remaining_characters = len(s) - start
            if remaining_characters < remaining_parts or remaining_characters > 3 * remaining_parts:
                return
            if len(parts) == 4:
                result.append(".".join(parts))
                return
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]
                if (part[0] == "0" and len(part) > 1) or int(part) > 255:
                    continue
                parts.append(part)
                backtrack(end, parts)
                parts.pop()

        backtrack(0, [])
        return result

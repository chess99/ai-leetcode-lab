# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not 4 <= len(s) <= 12:
            return []
        answer = []
        parts = []

        def backtrack(start: int) -> None:
            remaining_parts = 4 - len(parts)
            remaining_digits = len(s) - start
            if remaining_digits < remaining_parts or remaining_digits > 3 * remaining_parts:
                return
            if remaining_parts == 0:
                answer.append('.'.join(parts))
                return

            value = 0
            for end in range(start, min(start + 3, len(s))):
                if end > start and s[start] == '0':
                    break
                value = value * 10 + ord(s[end]) - ord('0')
                if value > 255:
                    break
                parts.append(s[start:end + 1])
                backtrack(end + 1)
                parts.pop()

        backtrack(0)
        return answer

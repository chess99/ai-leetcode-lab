# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def stringSequence(self, target: str) -> List[str]:
        answer = []
        prefix = ""
        for char in target:
            for code in range(ord('a'), ord(char) + 1):
                answer.append(prefix + chr(code))
            prefix += char
        return answer

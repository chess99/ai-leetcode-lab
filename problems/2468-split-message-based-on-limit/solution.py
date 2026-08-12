# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        length = len(message)
        digit_sum = 0
        parts = 0
        for total in range(1, length + 1):
            digit_sum += len(str(total))
            suffix_digits = len(str(total))
            capacity = (total * (limit - suffix_digits - 3)
                        - digit_sum)
            if capacity < length:
                continue
            if limit <= 2 * suffix_digits + 3:
                return []
            parts = total
            break
        if parts == 0:
            return []

        answer = []
        index = 0
        for part in range(1, parts + 1):
            suffix = f"<{part}/{parts}>"
            take = min(limit - len(suffix), length - index)
            answer.append(message[index:index + take] + suffix)
            index += take
        return answer

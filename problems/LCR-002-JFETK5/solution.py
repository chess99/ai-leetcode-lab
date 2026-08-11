# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:32:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index_a, index_b, carry = len(a) - 1, len(b) - 1, 0
        result = []
        while index_a >= 0 or index_b >= 0 or carry:
            total = carry
            if index_a >= 0:
                total += int(a[index_a])
                index_a -= 1
            if index_b >= 0:
                total += int(b[index_b])
                index_b -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))

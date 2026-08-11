# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:12:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        left, right = len(a) - 1, len(b) - 1
        carry = 0
        digits = []
        while left >= 0 or right >= 0 or carry:
            total = carry
            if left >= 0:
                total += ord(a[left]) - ord('0')
                left -= 1
            if right >= 0:
                total += ord(b[right]) - ord('0')
                right -= 1
            digits.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(digits))

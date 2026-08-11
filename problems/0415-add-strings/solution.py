# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        left, right = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        while left >= 0 or right >= 0 or carry:
            total = carry
            if left >= 0:
                total += ord(num1[left]) - ord("0")
                left -= 1
            if right >= 0:
                total += ord(num2[right]) - ord("0")
                right -= 1
            result.append(str(total % 10))
            carry = total // 10
        return "".join(reversed(result))

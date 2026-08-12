# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        modulus = (1 << 61) - 1
        base = 911382323
        def duplicate(length):
            power = pow(base, length, modulus)
            value = 0
            for index in range(length):
                value = (value * base + ord(s[index])) % modulus
            seen = {value: [0]}
            for start in range(1, len(s) - length + 1):
                value = (value * base - ord(s[start - 1]) * power + ord(s[start + length - 1])) % modulus
                for previous in seen.get(value, []):
                    if s[previous:previous + length] == s[start:start + length]:
                        return s[start:start + length]
                seen.setdefault(value, []).append(start)
            return ""
        left, right = 1, len(s) - 1
        answer = ""
        while left <= right:
            middle = (left + right) // 2
            found = duplicate(middle)
            if found:
                answer = found
                left = middle + 1
            else:
                right = middle - 1
        return answer

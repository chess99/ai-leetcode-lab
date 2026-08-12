# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:01:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not pattern:
            return not value
        count_a = pattern.count("a")
        count_b = len(pattern) - count_a
        if count_a < count_b:
            pattern = "".join("b" if char == "a" else "a" for char in pattern)
            count_a, count_b = count_b, count_a
        for length_a in range(len(value) // count_a + 1):
            remaining = len(value) - length_a * count_a
            if count_b == 0:
                if remaining:
                    continue
                length_b = 0
            elif remaining % count_b:
                continue
            else:
                length_b = remaining // count_b
            position = 0
            a = b = None
            valid = True
            for char in pattern:
                length = length_a if char == "a" else length_b
                piece = value[position:position + length]
                position += length
                if char == "a":
                    if a is None:
                        a = piece
                    elif a != piece:
                        valid = False
                        break
                else:
                    if b is None:
                        b = piece
                    elif b != piece:
                        valid = False
                        break
            if valid and a != b:
                return True
        return False

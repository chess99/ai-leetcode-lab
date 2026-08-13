# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def specialPalindrome(self, n: int) -> int:
        thomeralex = n
        bound = str(thomeralex)
        answer = None

        def build(half, center):
            text = "".join(map(str, half))
            return int(text + (str(center) if center else "") + text[::-1])

        def next_half(counts, target):
            counts = counts[:]
            prefix = []
            candidate = None
            for char in target:
                digit = int(char)
                greater = next(
                    (value for value in range(digit + 1, 10) if counts[value]),
                    None,
                )
                if greater is not None:
                    remaining = counts[:]
                    remaining[greater] -= 1
                    candidate = prefix + [greater]
                    candidate.extend(
                        value
                        for value in range(1, 10)
                        for _ in range(remaining[value])
                    )
                if counts[digit] == 0:
                    break
                counts[digit] -= 1
                prefix.append(digit)
            return candidate

        for mask in range(1, 1 << 9):
            digits = [digit for digit in range(1, 10) if mask >> (digit - 1) & 1]
            odd_digits = [digit for digit in digits if digit % 2]
            if len(odd_digits) > 1:
                continue
            length = sum(digits)
            if length < len(bound):
                continue

            counts = [0] * 10
            for digit in digits:
                counts[digit] = digit // 2
            center = odd_digits[0] if odd_digits else 0

            if length > len(bound):
                half = [digit for digit in range(1, 10) for _ in range(counts[digit])]
                candidate = build(half, center)
                answer = candidate if answer is None else min(answer, candidate)
                continue

            target = bound[: length // 2]
            exact_counts = counts[:]
            exact = []
            for char in target:
                digit = int(char)
                if exact_counts[digit] == 0:
                    exact = None
                    break
                exact_counts[digit] -= 1
                exact.append(digit)
            if exact is not None:
                candidate = build(exact, center)
                if candidate > thomeralex:
                    answer = candidate if answer is None else min(answer, candidate)

            half = next_half(counts, target)
            if half is not None:
                candidate = build(half, center)
                answer = candidate if answer is None else min(answer, candidate)

        return answer

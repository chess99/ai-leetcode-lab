# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:09:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        numbers = set()
        for first, a in enumerate(digits):
            if a == 0:
                continue
            for second, b in enumerate(digits):
                if second == first:
                    continue
                for third, c in enumerate(digits):
                    if third != first and third != second and c % 2 == 0:
                        numbers.add(100 * a + 10 * b + c)
        return sorted(numbers)

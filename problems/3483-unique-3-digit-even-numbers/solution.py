# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:02:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if len({i, j, k}) == 3 and digits[i] != 0 and digits[k] % 2 == 0:
                        numbers.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return len(numbers)

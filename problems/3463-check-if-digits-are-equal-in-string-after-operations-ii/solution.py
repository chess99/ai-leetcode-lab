# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        row = len(s) - 2
        small_choose = (
            (1, 0, 0, 0, 0),
            (1, 1, 0, 0, 0),
            (1, 2, 1, 0, 0),
            (1, 3, 3, 1, 0),
            (1, 4, 1, 4, 1),
        )

        def modulo_five(total: int, choose: int) -> int:
            result = 1
            while total or choose:
                a, b = total % 5, choose % 5
                if b > a:
                    return 0
                result = result * small_choose[a][b] % 5
                total //= 5
                choose //= 5
            return result

        difference = 0
        for i in range(row + 1):
            mod2 = int((i & ~row) == 0)
            mod5 = modulo_five(row, i)
            coefficient = mod5 if mod5 % 2 == mod2 else mod5 + 5
            difference += coefficient * (int(s[i]) - int(s[i + 1]))
        return difference % 10 == 0

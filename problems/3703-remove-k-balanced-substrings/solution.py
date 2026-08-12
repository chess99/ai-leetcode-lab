# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        merostalin = s
        runs = []

        def append(ch: str, count: int) -> None:
            if count == 0:
                return
            if runs and runs[-1][0] == ch:
                runs[-1][1] += count
            else:
                runs.append([ch, count])

        for ch in merostalin:
            append(ch, 1)
            while len(runs) >= 2 and runs[-2][0] == '(' and runs[-1][0] == ')' \
                    and runs[-2][1] >= k and runs[-1][1] >= k:
                runs[-2][1] -= k
                runs[-1][1] -= k
                right = runs.pop()[1]
                if runs[-1][1] == 0:
                    runs.pop()
                append(')', right)
        return ''.join(ch * count for ch, count in runs)

# AI solution attribution
# Original author: Codex Desktop / gpt-5.6-terra / medium / terra-medium
# Handoff: terra-medium WA on "gigigjjggjjgg" (2, expected 3)
# Current solver: Codex Desktop / gpt-5.6-sol / medium / sol-medium
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def makeStringGood(self, s: str) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        answer = len(s)  # Delete everything.
        for target in range(1, max(freq) + 1):
            # prev[keep] is the best cost through the previous letter, whose
            # final frequency is 0 when keep == 0 and target otherwise.
            prev = [freq[0], abs(freq[0] - target)]

            for i in range(1, 26):
                curr = [0, 0]
                for keep in range(2):
                    final = target if keep else 0
                    deficit = max(final - freq[i], 0)
                    unary_cost = abs(freq[i] - final)

                    best = float("inf")
                    for prev_keep in range(2):
                        prev_final = target if prev_keep else 0
                        surplus = max(freq[i - 1] - prev_final, 0)
                        saving = min(surplus, deficit)
                        best = min(best, prev[prev_keep] - saving)
                    curr[keep] = unary_cost + best
                prev = curr

            answer = min(answer, *prev)

        return answer

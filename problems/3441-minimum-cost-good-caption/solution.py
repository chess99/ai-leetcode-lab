# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""

        inf = 10**9
        next_cost = [inf, inf, 0] * 26
        decisions = bytearray(n * 26)
        start = 0

        for position in range(n - 1, -1, -1):
            original = ord(caption[position]) - 97
            switch_options = [
                (abs(original - char) + next_cost[char * 3], char)
                for char in range(26)
            ]
            switch_options.sort()
            cur = [inf] * 78
            for char in range(26):
                change = abs(original - char)
                cur[char * 3] = change + next_cost[char * 3 + 1]
                cur[char * 3 + 1] = change + next_cost[char * 3 + 2]

                best_switch = switch_options[0]
                if best_switch[1] == char:
                    best_switch = switch_options[1]
                same = (change + next_cost[char * 3 + 2], char)
                choice = min(same, best_switch)
                cur[char * 3 + 2] = choice[0]
                decisions[position * 26 + char] = choice[1]

            if position == 0:
                start = min(switch_options)[1]
            next_cost = cur

        output = [chr(start + 97)]
        char, run = start, 1
        for position in range(1, n):
            if run < 3:
                run += 1
            else:
                following = decisions[position * 26 + char]
                if following == char:
                    run = 3
                else:
                    char, run = following, 1
            output.append(chr(char + 97))
        return ''.join(output)

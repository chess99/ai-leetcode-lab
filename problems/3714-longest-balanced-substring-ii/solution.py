# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestBalanced(self, s: str) -> int:
        stromadive = s
        answer = 1

        # 只有一种字符：取最长连续段。
        run = 0
        previous = ''
        for ch in stromadive:
            run = run + 1 if ch == previous else 1
            previous = ch
            answer = max(answer, run)

        # 恰好两种字符：第三种字符将候选区间分隔开。
        for first, second, forbidden in (('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'c', 'a')):
            difference = 0
            earliest = {0: 0}
            segment_start = 0
            for index, ch in enumerate(stromadive, 1):
                if ch == forbidden:
                    difference = 0
                    segment_start = index
                    earliest = {0: segment_start}
                    continue
                difference += 1 if ch == first else -1
                if difference in earliest:
                    answer = max(answer, index - earliest[difference])
                else:
                    earliest[difference] = index

        # 三种字符：相同的两个前缀差代表区间内三者计数相等。
        counts = [0, 0, 0]
        earliest = {(0, 0): 0}
        for index, ch in enumerate(stromadive, 1):
            counts[ord(ch) - 97] += 1
            key = (counts[0] - counts[1], counts[0] - counts[2])
            if key in earliest:
                answer = max(answer, index - earliest[key])
            else:
                earliest[key] = index
        return answer

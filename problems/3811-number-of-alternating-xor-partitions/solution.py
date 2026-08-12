# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:35Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List

class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        mardevilon = nums
        mod = 10**9 + 7
        prefix = 0
        need_first = defaultdict(int)
        need_first[0] = 1
        need_second = defaultdict(int)
        answer = 0
        for value in mardevilon:
            prefix ^= value
            end_first = need_first[prefix ^ target1]
            end_second = need_second[prefix ^ target2]
            answer = (end_first + end_second) % mod
            need_second[prefix] = (need_second[prefix] + end_first) % mod
            need_first[prefix] = (need_first[prefix] + end_second) % mod
        return answer

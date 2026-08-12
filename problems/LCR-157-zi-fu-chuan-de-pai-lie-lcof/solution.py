# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def goodsOrder(self, goods: str) -> List[str]:
        chars, answer = sorted(goods), []
        def dfs(index):
            if index == len(chars): answer.append(''.join(chars)); return
            used = set()
            for i in range(index, len(chars)):
                if chars[i] in used: continue
                used.add(chars[i]); chars[index], chars[i] = chars[i], chars[index]
                dfs(index + 1); chars[index], chars[i] = chars[i], chars[index]
        dfs(0); return answer

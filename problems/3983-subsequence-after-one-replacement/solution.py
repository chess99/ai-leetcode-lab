# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        melvoritha = (s, t)
        if len(s) > len(t):
            return False
        exact = replaced = 0
        for char in t:
            previous_exact = exact
            if replaced < len(s) and s[replaced] == char:
                replaced += 1
            # 把当前待匹配字符替换成 char；本步必须基于更新前的 exact。
            if previous_exact < len(s):
                replaced = max(replaced, previous_exact + 1)
            if exact < len(s) and s[exact] == char:
                exact += 1
        return max(exact, replaced) == len(s)

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remaining={c:s.count(c) for c in set(s)}; stack=[]; used=set()
        for c in s:
            remaining[c]-=1
            if c in used: continue
            while stack and c<stack[-1] and remaining[stack[-1]]:
                used.remove(stack.pop())
            stack.append(c); used.add(c)
        return ''.join(stack)

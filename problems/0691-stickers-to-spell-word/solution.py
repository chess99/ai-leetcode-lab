# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        from collections import Counter
        from functools import lru_cache
        counts=[Counter(s)for s in stickers]
        @lru_cache(None)
        def solve(rest):
            if not rest:return 0
            need=Counter(rest);best=float('inf')
            for sticker in counts:
                if rest[0] not in sticker:continue
                remaining=''.join(c*(need[c]-sticker[c])for c in sorted(need)if need[c]>sticker[c])
                sub=solve(remaining)
                best=min(best,sub+1)
            return best
        answer=solve(''.join(sorted(target)));return -1 if answer==float('inf')else answer

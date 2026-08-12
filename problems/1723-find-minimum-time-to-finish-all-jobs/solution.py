# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True);load=[0]*k;best=sum(jobs)
        def dfs(i):
            nonlocal best
            if i==len(jobs):best=min(best,max(load));return
            seen=set()
            for w in range(k):
                if load[w]in seen or load[w]+jobs[i]>=best:continue
                seen.add(load[w]);load[w]+=jobs[i];dfs(i+1);load[w]-=jobs[i]
        dfs(0);return best

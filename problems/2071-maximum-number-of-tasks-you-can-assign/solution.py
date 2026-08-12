# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        from collections import deque
        tasks.sort();workers.sort()
        def ok(x):
            q=deque(); p=0; pills_left=pills
            for w in workers[-x:]:
                while p<x and tasks[p]<=w+strength:q.append(tasks[p]);p+=1
                if not q:return False
                if q[0]<=w:q.popleft()
                else:
                    if not pills_left:return False
                    pills_left-=1;q.pop()
            return True
        lo,hi=0,min(len(tasks),len(workers))
        while lo<hi:
            mid=(lo+hi+1)//2
            if ok(mid):lo=mid
            else:hi=mid-1
        return lo

# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        from collections import deque
        trees=sorted((value,r,c)for r,row in enumerate(forest)for c,value in enumerate(row)if value>1)
        def distance(sr,sc,tr,tc):
            queue=deque([(sr,sc,0)]);seen={(sr,sc)}
            while queue:
                r,c,d=queue.popleft()
                if (r,c)==(tr,tc):return d
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<len(forest)and 0<=nc<len(forest[0])and forest[nr][nc]and(nr,nc)not in seen:seen.add((nr,nc));queue.append((nr,nc,d+1))
            return -1
        r=c=answer=0
        for _,nr,nc in trees:
            steps=distance(r,c,nr,nc)
            if steps<0:return -1
            answer+=steps;r,c=nr,nc
        return answer

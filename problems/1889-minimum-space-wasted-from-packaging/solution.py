# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:51:59Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort();prefix=[0]
        for value in packages:prefix.append(prefix[-1]+value)
        best=10**30
        for sizes in boxes:
            sizes.sort()
            if sizes[-1]<packages[-1]:continue
            waste=0;start=0
            for size in sizes:
                end=bisect_right(packages,size,start)
                waste+=size*(end-start)-(prefix[end]-prefix[start]);start=end
            best=min(best,waste)
        return -1 if best==10**30 else best%1_000_000_007

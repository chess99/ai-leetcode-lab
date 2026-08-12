# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:08Z
# Experiment: ai-leetcode-lab, round 1
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1): left = mid + 1
            else: right = mid
        peak = left
        def search(left, right, ascending):
            while left <= right:
                mid = (left + right) // 2; value = mountainArr.get(mid)
                if value == target: return mid
                if (value < target) == ascending: left = mid + 1
                else: right = mid - 1
            return -1
        answer = search(0, peak, True)
        return answer if answer >= 0 else search(peak + 1, n - 1, False)

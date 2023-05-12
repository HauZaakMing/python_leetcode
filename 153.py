from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1


        while l<r:

            mid = (l+r)>>1
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]

s = Solution()
s.findMin([4,5,6,7,0,1,2])
from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l,r = 0,len(numbers)-1
        while l < r:
            mid = (l+r)>>1
            if numbers[mid]<numbers[r]:
                r = mid
            elif numbers[mid]>numbers[r]:
                l = mid+1
            else:
                r = r-1
        return numbers[r]

s = Solution()
s.minArray([3,3,1,3])
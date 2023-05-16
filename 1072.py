from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        s = {}
        ans = 0
        for i in range(len(matrix)):
            # 全零
            l_0 = [0 if num == 0 else 1 for num in matrix[i]]
            # 全一
            l_1 = [0 if num == 1 else 1 for num in matrix[i]]
            c0 = self.list2hashcode(l_0)
            c1 = self.list2hashcode(l_1)
            if s.get(c0) != None:
                s[c0] = s[c0]+1
            else:
                s[c0] = 1
            if s.get(c1) != None:
                s[c1] = s[c1]+1
            else:
                s[c1] = 1
            ans = max(s[c0],s[c1],ans)
        return  ans

    def list2hashcode(self,list:List[int]) -> int:
        code = 0
        for i in range(len(list)):
            code = (code<<1)+list[i]
        return code

s = Solution()
s.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]])
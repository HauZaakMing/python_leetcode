class Solution:
    def queryString(self, s: str, n: int) -> bool:
        set_seen = set()
        for i in range(len(s)):
            if s[i]== '0':
                continue
            else:
                j = i+1
                while j<len(s)+1:
                    num = int(s[i:j],2)
                    if(num<=n):
                        set_seen.add(num)
                    j = j+1
        if(len(set_seen)!=n):
            return False
        else:
            return True

s = Solution()
s.queryString("0110",3)

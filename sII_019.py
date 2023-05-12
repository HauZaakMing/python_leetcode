class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        flag = True
        while l<r:
            if s[l]==s[r]:
                l = l+1
                r = r-1
                continue
            else:
                if flag:
                    flag = False
                    # try l+1
                    l_1 = l+1
                    r_1 = r
                    while l_1<r_1:
                        if s[l_1] == s[r_1]:
                            l_1 = l_1+1
                            r_1 = r_1-1
                            continue
                        else:
                            break
                    if l_1>=r_1:
                        return True

                    # try r-1
                    l_1 = l
                    r_1 = r-1
                    while l_1 < r_1:
                        if s[l_1] == s[r_1]:
                            l_1 = l_1 + 1
                            r_1 = r_1 - 1
                            continue
                        else:
                            break
                    if l_1 >= r_1:
                        return True
                    return False
        return True
s = Solution()
s.validPalindrome("deeee")
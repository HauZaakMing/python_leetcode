class Solution:
    def fib(self, n: int) -> int:
        MOD = 10**9+7
        if n<2:
            return 1
        else:
            p = 1
            q = 1
            r = 0
            for i in range(n-1):
                r = (p+q)%MOD
                p = q
                q = r
        return r
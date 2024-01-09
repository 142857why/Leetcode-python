from functools import cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)

        @cache
        def f(i: int, cnt1: int, is_limit: bool) -> int:
            if i == len(s):
                return cnt1
            
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(up + 1):
                res += f(i + 1, cnt1 + (d == 1), is_limit and d == up)

            return res
        
        return f(0, 0, True)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countDigitOne(13))

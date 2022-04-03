class Solution:
    def numberOfWays(self, s: str) -> int:
        def numDistinct(s: str, t: str) -> int:
            # dp = [[0]*(len(s)+1)] * (len(t)+1)  # 初始化dp数组，加上两行空数组的情况
            dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
            for i in range(len(s) + 1):  # 空集是任意集合的子集  第一行赋值1
                dp[0][i] = 1

            for i in range(1, len(t) + 1):  # 控制行
                for j in range(1, len(s) + 1):  # 控制列
                    if s[j - 1] == t[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i][j - 1]
            return dp[-1][-1]

        ans = numDistinct(s, '010') + numDistinct(s, '101')
        return ans

if __name__ == '__main__':
    sol = Solution()
    st = '11100'
    print(sol.numberOfWays(st))

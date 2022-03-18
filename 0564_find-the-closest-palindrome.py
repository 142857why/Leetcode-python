class Solution:
    def nearestPalindromic(self, n: str) -> str:

        if int(n) < 10 or int(n[::-1]) == 1:  # 特殊情况1、2。解释一下int(n[::-1])，逆序以后数为1，原数不就是10的整数幂咯(不难理解)
            return str(int(n) - 1)

        l = len(n)
        candidates = [10 ** (l-1) - 1, 10 ** l + 1]
        selfPrefix = int(n[:(l + 1) // 2])
        for x in range(selfPrefix - 1, selfPrefix + 2):
            y = str(x) if l % 2 == 0 else str(x // 10)
            candidates.append(int(str(x) + y[::-1]))


        print('candidates = ', candidates)
        selfNumber = int(n)
        ans = -1
        for candidate in candidates:
            if candidate != selfNumber:
                if ans == -1 or \
                    abs(candidate - selfNumber) < abs(ans - selfNumber) or \
                        (abs(candidate - selfNumber) == abs(ans - selfNumber) and candidate < ans):

                    ans = candidate

        return str(ans)

if __name__ == '__main__':
    sol = Solution()
    n = '100000'
    print(sol.nearestPalindromic(n))
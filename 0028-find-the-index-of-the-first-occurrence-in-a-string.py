class Solution:
    def z_function(self, s):
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r and z[i - l] < r - i + 1:
                z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        return z
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        z = self.z_function(needle + '#' + haystack)
        for i in range(len(needle) + 1, len(z)):
            if z[i] == len(needle):
                return i - len(needle) - 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr('hello', 'll'))
    print(sol.strStr('aaaaa', 'bba'))
    print(sol.strStr('aaaaa', ''))

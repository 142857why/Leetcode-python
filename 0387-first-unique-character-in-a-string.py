class Solution:
    def firstUniqChar(self, s: str) -> int:
        position = dict()
        n = len(s)
        for i, ch in enumerate(s):
            if ch in position:
                position[ch] = -1
            else:
                position[ch] = i

        res = n
        for pos in position.values():
            if pos != -1 and pos < res:
                res = pos

        if res == n:
            res = -1

        return res


if __name__ == '__main__':
    sol = Solution()
    s = 'leetcode'
    print(sol.firstUniqChar(s))
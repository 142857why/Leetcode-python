class Solution:
    def maximumLength(self, s: str) -> int:
        def occurrences(string, sub):
            count = start = 0
            while True:
                start = string.find(sub, start) + 1
                if start > 0:
                    count += 1
                else:
                    return count

        n = len(s)
        # 从n-3开始往下遍历
        for i in range(n - 2, 0, -1):
            # 字母c从'a'到'z'遍历
            for c in range(ord('a'), ord('z') + 1):
                # 构造一个长度为i的字符串, 里面全是字母c
                t = chr(c) * i
                if occurrences(s, t) >= 3:
                    return i

        return -1


if __name__ == '__main__':
    solution = Solution()
    # 随机生成一个长度大概为100000的字符串，里面全是小写字母
    import random
    import string
    # 固定随机数种子，保证每次运行生成的随机数都是一样的
    random.seed(7)
    n = 10000
    s = ''.join(random.choices(string.ascii_lowercase, k=n))
    print(s)
    print(solution.maximumLength(s))

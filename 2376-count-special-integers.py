from functools import cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)

        @cache
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            print('mask = ', bin(mask))
            if i == len(s):
                return 1 if is_num else 0

            res = 0
            if not is_num:
                # is_num代表前面是(True)否(False)填了数字, 也其实是对有没有前导0的判断
                # 如果前面没有填写数字则会执行到这里
                res = f(i + 1, mask, False, False)

            up = int(s[i]) if is_limit else 9  # 如果是限制的则只能填写比s[i]小的数字

            # 枚举要在位置i上填写的数字，由有没有前导0决定了从0还是从1开始枚举
            # 如果is_num == True, 则从0开始枚举. 这是因为前面已经填写了数字, 所以可以填写0
            # 如果is_num == False, 则从1开始枚举. 这是因为前面没有填写数字, 所以不能填写0
            for d in range(1 - int(is_num), up + 1):
                if mask & (1 << d) == 0:
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True)

            return res

        return f(0, 0, True, False)


if __name__ == '__main__':
    solution = Solution()

    print(solution.countSpecialNumbers(20))
    # print(solution.countSpecialNumbers(135))

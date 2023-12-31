from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        runs = defaultdict(list)
        cnt = 0
        for i, ch in enumerate(s):
            cnt += 1
            if i == n - 1 or s[i + 1] != ch:
                li = runs[ch]
                # 只维护前三大值
                match len(li):
                    case 0:
                        li.append(cnt)
                    case 1:
                        if cnt > li[0]:
                            li.insert(0, cnt)
                        else:
                            li.append(cnt)
                    case 2:
                        if cnt > li[0]:
                            li.insert(0, cnt)
                        elif cnt > li[1]:
                            li.insert(1, cnt)
                        else:
                            li.append(cnt)
                    case 3:
                        if cnt > li[0]:
                            li[0], li[1], li[2] = cnt, li[0], li[1]
                        elif cnt > li[1]:
                            li[1], li[2] = cnt, li[1]
                        elif cnt > li[2]:
                            li[2] = cnt

                cnt = 0

        ans = 0
        for li in runs.values():
            li.extend([0, 0])
            ans = max(ans, li[0] - 2, min(li[0] - 1, li[1]), li[2])

        return ans if ans else -1


if __name__ == '__main__':
    solution = Solution()
    import random
    import string

    random.seed(7)
    n = 10000
    s = ''.join(random.choices(string.ascii_lowercase, k=n))
    # print(s)
    print(solution.maximumLength(s))
    s = "abcaba"
    print(solution.maximumLength(s))
    s = "aabca"
    print(solution.maximumLength(s))

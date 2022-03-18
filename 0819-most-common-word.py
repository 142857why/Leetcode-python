import collections
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        count = collections.Counter(paragraph.lower().split())
        # print(count)

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans

if __name__ == '__main__':
    sol = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."

    banned = ["hit"]
    print(sol.mostCommonWord(paragraph, banned))
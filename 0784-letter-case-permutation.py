from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        self.dfs(s, 0, [], results)
        return results

    def dfs(self, s: str, startIndex: int, subset: List[str], results: List[List[str]]) -> None:
        if startIndex == len(s):
            results.append(''.join(subset))
            return

        if s[startIndex].isdigit():
            subset.append(s[startIndex])
            self.dfs(s, startIndex + 1, subset, results)
            subset.pop()
        else:
            subset.append(s[startIndex].lower())
            self.dfs(s, startIndex + 1, subset, results)
            subset.pop()

            subset.append(s[startIndex].upper())
            self.dfs(s, startIndex + 1, subset, results)
            subset.pop()


if __name__ == '__main__':
    solution = Solution()
    s = 'a1b2'
    print(solution.letterCasePermutation(s))
    s = '3z4'
    print(solution.letterCasePermutation(s))
    s = '12345'
    print(solution.letterCasePermutation(s))
    s = '0'
    print(solution.letterCasePermutation(s))
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 已经保证 begin, end, wordList里面的单词长度均相同
        pass


if __name__ == '__main__':
    beginWord = 'hit'
    endWord = 'cog'
    l = ["hot","dot","dog","lot","log","cog"]
    sol = Solution()
    print(sol.ladderLength(beginWord, endWord, l))
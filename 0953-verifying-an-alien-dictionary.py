from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c : i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    # The first difference that word1[k] != word2[k]
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    else:
                        # the word is in order
                        break
                else:
                    continue # Continue to compare
            else:
                if len(word1) > len(word2):
                    return False

        return True


if __name__ == '__main__':
    sol = Solution()
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(sol.isAlienSorted(words, order))
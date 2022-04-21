class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        res = sentence.split()
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i in range(len(res)):
            if res[i][0] in vowel:
                ans.append(res[i] + 'ma' + 'a' * (i + 1))
            else:
                ans.append(res[i][1:] + res[i][0] + 'ma' + 'a' * (i + 1))

        return ' '.join(ans)


if __name__ == '__main__':
    s = "I speak Goat Latin"
    sol = Solution()
    print(sol.toGoatLatin(s))

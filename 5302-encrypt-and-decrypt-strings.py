from typing import List
from collections import defaultdict


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.d = defaultdict(int)
        self.m = {}
        for i, j in zip(keys, values):
            self.m[i] = j

        for i in dictionary:
            l = []
            for x in i:
                l.append(self.m[x])
            self.d[''.join(l)] += 1

        print(self.d)
        print(self.m)


    def encrypt(self, word1: str) -> str:
        return ''.join(self.m[x] for x in word1)

    def decrypt(self, word2: str) -> int:
        return self.d[word2]


if __name__ == '__main__':
    '''
    encrypter.encrypt("abcd"); // 返回 "eizfeiam"。 
                           // 'a' 映射为 "ei"，'b' 映射为 "zf"，'c' 映射为 "ei"，'d' 映射为 "am"。
    encrypter.decrypt("eizfeiam"); // return 2. 
                              // "ei" 可以映射为 'a' 或 'c'，"zf" 映射为 'b'，"am" 映射为 'd'。 
                              // 因此，解密后可以得到的字符串是 "abad"，"cbad"，"abcd" 和 "cbcd"。 
                              // 其中 2 个字符串，"abad" 和 "abcd"，在 dictionary 中出现，所以答案是 2 。
    '''


    keys = ['a', 'b', 'c', 'd']
    values = ["ei", "zf", "ei", "am"]
    dictionary = ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]
    # 字典代表所有允许出现的字符
    obj = Encrypter(keys, values, dictionary)
    print(obj.encrypt("abcd"))
    print(obj.decrypt("eizfeiam"))
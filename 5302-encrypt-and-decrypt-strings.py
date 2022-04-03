from typing import List


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self._keys = keys
        self._values = values
        self._dictionary = dictionary

    def encrypt(self, word1: str) -> str:
        return ''.join(values[keys.index(x)] for x in word1)

    def decrypt(self, word2: str) -> int:
        pass


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
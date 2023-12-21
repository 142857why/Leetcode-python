class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_word = True
        node.word = word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    print(obj.search("apple"))
    print(obj.search("app"))
    print(obj.startsWith("app"))
    obj.insert("app")
    print(obj.search("app"))
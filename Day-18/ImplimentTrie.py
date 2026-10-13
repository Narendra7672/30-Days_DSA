# Implement Trie (Prefix Tree):
class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return "#" in node
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))     # True
print(trie.search("app"))       # False
print(trie.startsWith("app"))   # True
trie.insert("app")

print(trie.search("app"))       # True
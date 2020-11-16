class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = set()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.trie.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.trie:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for ele in self.trie:
            if len(ele) < len(prefix):
                continue
            else:
                if prefix == ele[:len(prefix)]:
                    return True
        return False

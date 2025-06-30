class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.word

    def search_prefix(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# Test
trie = Trie()

trie.insert_word('nathanael')
trie.insert_word('joshua')
trie.insert_word('kidus')

print(trie.search_word('nathanael'))
print(trie.search_word('josh'))
print(trie.search_word('kidus'))
print(trie.search_word('kiduscheramlak'))

print(trie.search_prefix('nat'))
print(trie.search_prefix('nati'))
print(trie.search_prefix('kidus'))
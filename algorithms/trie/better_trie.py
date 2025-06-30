from collections import deque

class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
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

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        found_words = []

        # DFS Implementation
        def dfs(node, path):
            path.append(node.char)
            if not node.children and node.word:
                current_word = ''.join(path)
                found_words.append(word[:-1] + current_word)
                return 
            
            if node.word:
                current_word = ''.join(path)
                found_words.append(word[:-1] + current_word)
            
            for child in node.children.values():
                dfs(child, path)
                path.pop()

        dfs(curr, [])
        return found_words
    
# Test
trie = Trie()

trie.insert_word('nathanael')
trie.insert_word('natiman')
trie.insert_word('joshua')
trie.insert_word('kidus')
trie.insert_word('josh')


print(trie.search_word('nathanael'))
print(trie.search_word('josh'))
print(trie.search_word('kidus'))
print(trie.search_word('kiduscheramlak'))

print(trie.search_prefix('nat'))
print(trie.search_prefix('nati'))
print(trie.search_prefix('kidus'))

print(trie.search("jo"))
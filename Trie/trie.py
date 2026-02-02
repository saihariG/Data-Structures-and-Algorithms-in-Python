# A trie node represents a single alphabet of the word
# Root Node is always empty. All the words inserted into the Trie originate after the root node

# Representation of a TrieNode
# It consists of two data members
# 1. An array which refers to other TrieNode's in a Trie, also called the child nodes of a TrieNode
#    The Size of this array is usually 26 (representing the English alphabets)
# 2. A boolean to indicate the end of word. This value is set as true when a word is inserted completely
class TrieNode:
    def __init__(self):
        # Character to index mapping - a -> 0th index .... z -> 25th index
        self.children = [None] * 26
        self.is_word = False


# Applications:
# 1. Fast Prefix searches 
# 2. Auto-complete
# 3. Dictionary / spell checker
class Trie:

    # A root TrieNode is at top with empty value having 26 links (one per alphabet)
    # The links are either null or points to another TrieNode
    def __init__(self):
        self.root = TrieNode()


    # Case 1: Inserting in an empty Trie
    # case 2: Inserting a new word 
    # case 3: Inserting a word with common prefix
    # case 4: Inserting a word which is already present
    def insert(self, word):
        if word is None or len(word) == 0:
            return
        
        word = word.lower()
        current = self.root

        for ch in word:
            index = ord(ch) - ord('a')

            if(current.children[index] is None):
                node = TrieNode()
                current.children[index] = node
                current = node
            else:
                current = current.children[index]

        current.isWord = True

    def delete(self, word):
        current = self.root

        for ch in word:
            index = ord(ch) - ord('a')

            if(current.children[index] is None):
                print("Word is not present")
                return
            else:
                current = current.children[index]
        
        if current.is_word:
            current.is_word = False
            print("Word deleted from Trie")
        else:
            print("Word not present")

    def search(self, word):
        current = self.root 

        for ch in word:
            index = ord(ch) - ord('a')

            if current.children[index] is None:
                return False
            else:
                current = current.children[index]

        if current.is_word:
            return True
        
        return False
    

if __name__ == "__main___":
    trie = Trie()

    trie.insert("cat")
    trie.insert("cab")
    trie.insert("son")
    trie.insert("so")

    trie.search("cab")
    trie.search("cat")

    trie.search("can")

    trie.delete("cat")
    trie.delete("can")

    trie.search("cat")

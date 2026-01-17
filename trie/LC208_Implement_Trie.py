#!/usr/bin/env python3
"""
208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() 
Initializes the trie object.

void insert(String word) 
Inserts the string word into the trie.

boolean search(String word) 
Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.

boolean startsWith(String prefix) 
Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

Topics
Hash Table
String
Design
Trie


Developer Insights
Problem Nature
We must design a Trie (prefix tree) supporting:
insert(word): add a word.
search(word): check if word exists.
startsWith(prefix): check if any word starts with prefix.
This is a Design + Trie problem: requires efficient prefix storage and retrieval.

Key Observations
Trie nodes store:
Children (dict mapping char → node).
End‑of‑word flag.

Operations:
Insert: traverse characters, create nodes if missing, mark end.
Search: traverse characters, check existence, verify end flag.
StartsWith: traverse characters, check existence, no need for end flag.

Complexity:
Insert: O(L)
Search: O(L)
StartsWith: O(L)
where L = length of word/prefix.

Strategy
Define TrieNode class with children + end flag.
Define Trie class with root node.
Implement insert, search, startsWith.
Use dictionary for children mapping.
Edge cases: empty strings, repeated inserts, prefixes overlapping.

Complexity
Time: O(L) per operation.
Space: O(N · L) worst case (N words, length L).


Pseudocode
class TrieNode:
    children = {}
    is_end = False

class Trie:
    root = TrieNode()

    insert(word):
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    search(word):
        node = root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    startsWith(prefix):
        node = root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

"""


from typing import Dict


class TrieNode:
    """
    Node in a Trie (Prefix Tree).

    Attributes:
        children (Dict[str, TrieNode]): Mapping from character to child node.
        is_end (bool): Flag indicating if node marks end of a word.
    """
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.is_end: bool = False

    def __repr__(self) -> str:
        return f"TrieNode(end={self.is_end}, children={list(self.children.keys())})"


class Trie:
    """
    Trie (Prefix Tree) data structure.

    Supports:
        - insert(word): Add a word to the trie.
        - search(word): Check if word exists in the trie.
        - startsWith(prefix): Check if any word starts with prefix.

    Design:
        - Root node is empty.
        - Each node stores children and end flag.
        - Operations traverse character by character.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.

        Args:
            word (str): Word to insert.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the trie.

        Args:
            word (str): Word to search.

        Returns:
            bool: True if word exists, False otherwise.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Check if any word in the trie starts with the given prefix.

        Args:
            prefix (str): Prefix to check.

        Returns:
            bool: True if prefix exists, False otherwise.
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))    # Expected: True
    print(trie.search("app"))      # Expected: False
    print(trie.startsWith("app"))  # Expected: True
    trie.insert("app")
    print(trie.search("app"))      # Expected: True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

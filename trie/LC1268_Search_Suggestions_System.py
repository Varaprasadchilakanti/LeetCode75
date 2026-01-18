#!/usr/bin/env python3
"""
1268. Search Suggestions System

You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.

Constraints:
1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.

Topics
Array
String
Binary Search
Trie
Sorting
Heap (Priority Queue)
Weekly Contest 164

Hint 1
Brute force is a good choice because length of the string is ≤ 1000.
Hint 2
Binary search the answer.
Hint 3
Use Trie data structure to store the best three matching. Traverse the Trie.


Developer Insights
Problem Nature
We must design a system that suggests up to three lexicographically smallest products after each character of searchWord is typed.
This is a Trie + Sorting + Prefix Search problem.

Key Observations
Products must be sorted lexicographically.
After each prefix of searchWord, we need at most 3 matches.
Efficient approaches:
Trie: store products, each node keeps top 3 lexicographically smallest suggestions.
Binary Search: maintain sorted list, use prefix bounds.
Constraints allow either, but Trie is canonical here.

Strategy
Preprocess products: sort lexicographically.
Build Trie:
Each node stores children and a list of up to 3 suggestions.
While inserting, append product to node’s suggestion list (keep ≤ 3).

Query:
Traverse Trie for each prefix of searchWord.
Collect suggestions at each node.
If prefix not found, append empty lists for remaining characters.

Complexity
Build Trie: O(sum(len(product))).
Query: O(len(searchWord)).
Each node stores ≤ 3 suggestions → space efficient.

Edge Cases
Single product → always suggested.
No matching prefix → empty lists.
Large product lengths (≤ 3000) handled by Trie.
Lexicographic order guaranteed by preprocessing.


Pseudocode
class TrieNode:
    children = {}
    suggestions = []

class Trie:
    root = TrieNode()

    insert(word):
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if len(node.suggestions) < 3:
                node.suggestions.append(word)

    getSuggestions(prefix):
        node = root
        result = []
        for ch in prefix:
            if ch not in node.children:
                result.append([])
                node = None
            else:
                node = node.children[ch]
                result.append(node.suggestions)
        return result

"""

from typing import List, Dict, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class SuggestionStrategy(Protocol):
    """
    Protocol defining the interface for search suggestion strategies.
    """
    def solve(self, products: List[str], searchWord: str) -> List[List[str]]: ...


# ───────────────────────────────────────────────────────────────────────────
# Trie Node
# ───────────────────────────────────────────────────────────────────────────

class TrieNode:
    """
    Node in a Trie storing children and up to 3 lexicographically smallest suggestions.
    """
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.suggestions: List[str] = []

    def __repr__(self) -> str:
        return f"TrieNode(suggestions={self.suggestions}, children={list(self.children.keys())})"


# ───────────────────────────────────────────────────────────────────────────
# Trie Strategy
# ───────────────────────────────────────────────────────────────────────────

class TrieSuggestionStrategy:
    """
    Trie-based strategy for search suggestions.

    Design:
        - Sort products lexicographically.
        - Insert each product into Trie.
        - Each node stores up to 3 suggestions.
        - Query by traversing prefix nodes.

    Time Complexity:
        - Build: O(sum(len(product)))
        - Query: O(len(searchWord))
    Space Complexity: O(sum(len(product)))
    """

    def solve(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()

        # Build Trie
        for word in products:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(node.suggestions) < 3:
                    node.suggestions.append(word)

        # Query
        result, node = [], root
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                result.append(node.suggestions)
            else:
                node = None
                result.append([])
        return result


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates search suggestion computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Trie strategy
    """

    def __init__(self, strategy: SuggestionStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else TrieSuggestionStrategy()

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Entry point for LeetCode.

        Args:
            products (List[str]): List of product names.
            searchWord (str): Search word typed by user.

        Returns:
            List[List[str]]: Suggestions after each character typed.
        """
        return self.strategy.solve(products, searchWord)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()
    print(solution.suggestedProducts(
        ["mobile","mouse","moneypot","monitor","mousepad"], "mouse"
    ))  # Expected: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

    print(solution.suggestedProducts(["havana"], "havana"))  # Expected: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

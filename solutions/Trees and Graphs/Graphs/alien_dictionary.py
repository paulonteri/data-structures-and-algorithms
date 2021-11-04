""" 
269. Alien Dictionary:

There is a new alien language that uses the English alphabet. 
However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. 
If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, 
    the letter in s comes before the letter in t in the alien language. 
If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.


Test cases:
    ["wrt", "wrf", "er", "ett", "rftt"]
    ["z", "x"]
    ["z", "x", "z"]
    ["ab", "adc"]
    ["z", "z"]
    ["abc", "ab"]
    ["z", "x", "a", "zb", "zx"]
    ["w", "wnlb"]
    ["wnlb"]
    ["aba"]

Results:
    "wertf"
    "zx"
    ""
    "abcd"
    "z"
    ""
    ""
    "wnlb"
    "wnlb"
    "ab"

['f', 't', 'r', 'e', 'w']
['x', 'z']
['x', 'z']
['a', 'd', 'b', 'c']
['z']
['a', 'x', 'z', 'b']
['w', 'n', 'l', 'b']
['w', 'n', 'l', 'b']
['a', 'b']

https://leetcode.com/problems/alien-dictionary/

"""
import collections

""" 
A few things to keep in mind:
    - The letters within a word don't tell us anything about the relative order. 
        For example, the presence of the word kitten in the list does not tell us that the letter k is before the letter i.
    - The input can contain words followed by their prefix, for example, abcd and then ab. 
        These cases will never result in a valid alphabet (because in a valid alphabet, prefixes are always first). 
        You'll need to make sure your solution detects these cases correctly.
    - There can be more than one valid alphabet ordering. It is fine for your algorithm to return any one of them.
    - Your output string must contain all unique letters that were within the input list, including those that could be in any position within the ordering. 
        It should not contain any additional letters that were not in the input.

All approaches break the problem into three steps:
    - Extracting dependency rules from the input. 
        For example "A must be before C", "X must be before D", or "E must be before B".
    - Putting the dependency rules into a graph with letters as nodes and dependencies as edges (an adjacency list is best).
    - Topologically sorting the graph nodes

"""


class Solution:
    def alienOrder(self, words):
        graph = collections.defaultdict(set)  # Adjacency list

        # build graph
        for idx in range(len(words)):
            self.add_word_letters(graph, words[idx])

            # if not at end
            if idx < len(words)-1:
                self.add_word_letters(graph, words[idx+1])
                if not self.compare_two_words(graph, words[idx], words[idx+1]):
                    return ""

        return "".join(self.top_sort(graph))

    def top_sort(self, graph):
        """ 
        Topological sort

        Remember that: 
            If the number of nodes in the the top sort result is
            less than the number of nodes in the graph, we have a cycle.
            Which means that we cannot have a valid ordering. Return []
        """
        res = []

        queue = []
        indegrees = collections.defaultdict(int)

        # calculate indegrees
        for node in graph:
            for child in graph[node]:
                indegrees[child] += 1

        # get sources
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)

        # sort
        while queue:
            node = queue.pop(0)
            res.append(node)  # Add to result

            for child in graph[node]:
                indegrees[child] -= 1
                if indegrees[child] == 0:  # Has become a source
                    queue.append(child)

        # check if has_cycle
        if len(res) != len(graph):
            return []
        return res

    def compare_two_words(self, graph, one, two):
        """
        Where two words are adjacent, we need to look for the first difference between them. 
        That difference tells us the relative order between two letters.

        Handle edge cases like:
            ab, a => error(a should be before ab)
        """

        idx = 0
        while idx < len(one) and idx < len(two) and one[idx] == two[idx]:
            idx += 1

        if idx < len(one) and idx < len(two):
            graph[one[idx]].add(two[idx])
        elif idx < len(one):
            return False  # Invalid

        return True

    def add_word_letters(self, graph, word):
        for idx in range(len(word)):
            graph[word[idx]]  # Add letter to graph.


"""  

DFS / reveese of Topological sort

"""


class SolutionDFS:
    def alienOrder(self, words):
        graph = collections.defaultdict(set)  # Adjacency list

        # build graph
        for idx in range(len(words)):
            self.add_word_letters(graph, words[idx])

            # if not at end
            if idx < len(words)-1:
                self.add_word_letters(graph, words[idx+1])
                if not self.compare_two_words(graph, words[idx], words[idx+1]):
                    return ""

        if self.has_cycle(graph):
            return ""
        return "".join(reversed(self.dfs(graph)))

    def compare_two_words(self, graph, one, two):
        """
        Where two words are adjacent, we need to look for the first difference between them. 
        That difference tells us the relative order between two letters.

        Handle edge cases like:
            ab, a => error(a should be before ab)
        """

        idx = 0
        while idx < len(one) and idx < len(two) and one[idx] == two[idx]:
            idx += 1

        if idx < len(one) and idx < len(two):
            graph[one[idx]].add(two[idx])
        elif idx < len(one):
            return False  # Invalid

        return True

    def add_word_letters(self, graph, word):
        for idx in range(len(word)):
            graph[word[idx]]  # Add letter to graph.

    def dfs(self, graph):
        """ 
        DFS => reveese of Topological sort

        Remember that: 
            If the number of nodes in the the top sort result is
            less than the number of nodes in the graph, we have a cycle.
            Which means that we cannot have a valid ordering. Return []
        """
        res = []
        visited = set()
        for node in graph:
            self.dfs_helper(graph, visited, node, res)

        # check if has_cycle
        if len(res) != len(graph):
            return []
        return res

    def dfs_helper(self, graph, visited,  curr, res):
        if curr in visited:
            return

        visited.add(curr)
        for node in graph[curr]:
            self.dfs_helper(graph, visited, node, res)

        res.append(curr)

    def has_cycle(self, graph):
        checked = {}

        for node in graph:
            if self._has_cycle_helper(graph, checked, set(), node):
                return True
        return False

    def _has_cycle_helper(self, graph, checked, visiting, node):
        if node in visiting:
            return True
        if node in checked:
            return checked[node]

        visiting.add(node)

        result = False
        for child in graph[node]:
            result = result or self._has_cycle_helper(
                graph, checked, visiting, child)

        # remember to add this!
        #   because it is a directed graph
        #   we might reach the node several times but it doesn't mean it is is a cycle
        #   eg: https://www.notion.so/paulonteri/Searching-733ff84c808c4c9cb5c40787b2df7b98#c7458268f05e4e2db359f9990366a411
        visiting.discard(node)

        checked[node] = result
        return checked[node]

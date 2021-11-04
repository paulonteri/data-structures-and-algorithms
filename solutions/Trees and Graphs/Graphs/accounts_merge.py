""" 
Accounts Merge:

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. 
Two accounts definitely belong to the same person if there is some common email to both accounts. 
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. 
A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

    Input: 
        accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    Output: 
        [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    Explanation:
    The first and second John's are the same person as they have the common email "johnsmith@mail.com".
    The third John and Mary are different people as none of their email addresses are used by other accounts.
    We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
    ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:
    Input: 
        accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
    Output: 
        [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

https://leetcode.com/problems/accounts-merge
"""
import collections


"""
-------------------- Problem --------------------
accounts[i][0] is a name, and the rest of the elements are emails 
Two accounts definitely belong to the same person if there is some common email to both accounts
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. 
A person can have any number of accounts initially, but all of their accounts definitely have the same name.


-------------------- Examples --------------------
accounts = [
["John","johnsmith@mail.com","john_newyork@mail.com"],                  ["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],   
["John","johnnybravo@mail.com"]]

Output: [
["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]


-------------------- Brute force --------------------
O(n^2) time | O(n) space
- for every account, look for duplicates


-------------------- Optimal --------------------

- build undirected cyclic graph of the emails
- dfs/bfs returning all connected emails
- add name to connected emails

[["D","d0@m.co","d1@m.co","d9@m.co","d8@m.co"],["D","d3@m.co","d4@m.co"],["D","d4@m.co","d5@m.co"],["D","d2@m.co","d3@m.co"],["D","d1@m.co","d2@m.co"]]


[
["D","d0@m.co","d1@m.co","d9@m.co","d8@m.co"],
["D","d3@m.co","d4@m.co"],
["D","d4@m.co","d5@m.co"],
["D","d6@m.co","d8@m.co"]
["D","d2@m.co","d3@m.co"],
["D","d1@m.co","d2@m.co"]

]

(only using the number part of the email)
# use the first email as the original key and let the others point to it

--- idx 0 ["D","d0@m.co","d1@m.co","d9@m.co","d8@m.co"]
0:[1,9,8]*
1:[0]*
9:[0]*
8:[0]*
--- ["D","d3@m.co","d4@m.co"]
0:[1,9,8]
1:[0]
9:[0]
8:[0]
3:[4]*
4:[3]*
--- ["D","d4@m.co","d5@m.co"]
0:[1,9,8]
1:[0]
9:[0]
8:[0]
3:[4]
4:[3,5]*
5:[4]*
--- ["D","d6@m.co","d8@m.co"]
0:[1,9,8]
1:[0]
9:[0]
8:[0]
3:[4]
4:[3,5]
5:[4]
6:[8]*
8:[6]*
--- ["D","d2@m.co","d3@m.co"],
0:[1,9,8]
1:[0]
9:[0]
8:[0]
3:[4,2]*
4:[3,5]
5:[4]
6:[8]
8:[6]
2:[3]*
--- ["D","d1@m.co","d2@m.co"]
0:[1,9,8]
1:[0,2] *
9:[0]
8:[0]
3:[4,2]
4:[3,5]
5:[4]
6:[8]
8:[6]
2:[3,1] *
---
after dfs
[0,1,2,3,4,5,9,8]
[6,8]

"""


class Solution:
    def accountsMerge(self, accounts):
        result = []

        email_to_name = {}
        graph = collections.defaultdict(list)  # Adjacency List
        for account in accounts:
            name = account[0]
            main_email = account[1]

            # add emails to graph
            for idx in range(1, len(account)):
                # point to each other
                graph[main_email].append(account[idx])
                graph[account[idx]].append(main_email)
                # save name
                email_to_name[account[idx]] = name

        visited = set()
        for node in graph:
            emails_found = set()
            self.dfs(graph, node, visited, emails_found)
            if emails_found:
                sorted_emails = sorted(list(emails_found))
                name = email_to_name[sorted_emails[0]]
                result.append([name]+sorted_emails)
        return result

    def dfs(self, graph, node, visited, emails_found):
        if node in visited:
            return
        visited.add(node)

        # add node to emails_found
        emails_found.add(node)

        for email in graph[node]:
            self.dfs(graph, email, visited, emails_found)

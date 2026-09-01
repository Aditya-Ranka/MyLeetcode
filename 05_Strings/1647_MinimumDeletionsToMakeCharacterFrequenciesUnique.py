"""
Problem: Minimum Deletions to Make Character Frequencies Unique
LeetCode: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
Topic: Strings
Difficulty: Medium

Approach:
- Count occurrences of each character in the string using a hashmap.
- Initialize a set to store frequencies that have already been used and a counter for deletions.
- For each character's frequency, repeatedly decrement it (counting a deletion each time) until the frequency is either zero or not present in the set.
- Add the final (possibly zero) frequency to the set and continue with the next character.
- Return the total number of deletions performed.

Comments:
- A zero frequency is still added to the set, but the loop stops at freq > 0, preventing an infinite loop.
- The algorithm works without sorting because it always reduces a duplicate frequency to the nearest lower unused value, which is optimal.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        res = 0
        freqs = set()
        for c, freq in count.items():
            while freq > 0 and freq in freqs:
                freq -= 1 
                res+=1
            freqs.add(freq)
        return res

"""
Problem: Isomorphic Strings
LeetCode: https://leetcode.com/problems/isomorphic-strings/
Topic: Strings
Difficulty: Easy

Approach:
- Check if lengths differ and return False if so
- Create two empty dictionaries for forward and reverse character mappings
- Iterate over each index, retrieve characters a from s and b from t
- If a already has a mapping, verify it matches b; otherwise return False
- If a is new, ensure b is not already mapped to another character, then record both mappings
- After processing all positions, return True

Comments:
- Uses two hash maps to guarantee a one-to-one correspondence, preventing multiple s‑chars mapping to the same t‑char
- Runs in O(n) time and O(k) extra space where k is the number of distinct characters

Time Complexity: O(n)
Space Complexity: O(k)
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_st = {}   
        map_ts = {}   

        for i in range(len(s)):
            a, b = s[i], t[i]
            if a in map_st:
                if map_st[a] != b:
                    return False
            else:
                if b in map_ts:
                    return False
                map_st[a] = b
                map_ts[b] = a

        return True

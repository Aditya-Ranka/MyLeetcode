"""
Problem: Reverse Words in a String
LeetCode: https://leetcode.com/problems/reverse-words-in-a-string/
Topic: Sliding Window / Two Pointer
Difficulty: Medium

Approach:
- Trim leading and trailing spaces from s
- Iterate characters of the trimmed string in reverse order
- Accumulate non‑space characters on a stack until a space is seen
- When a space is encountered, pop the stack to output the word in correct order and add a single space
- After the loop, flush any remaining characters for the first word

Comments:
- Handles multiple consecutive spaces by checking if the stack is empty; returns an empty string for input consisting only of spaces

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()          
        stck = []
        res = []

        for char in reversed(s):
            if char != " ":
                stck.append(char)
            else:
                if stck:        
                    while stck:
                        res.append(stck.pop())
                    res.append(" ")

        if stck:               
            while stck:
                res.append(stck.pop())

        return ''.join(res)

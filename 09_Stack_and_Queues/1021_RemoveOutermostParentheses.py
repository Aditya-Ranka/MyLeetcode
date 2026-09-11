"""
Problem: Remove Outermost Parentheses
LeetCode: https://leetcode.com/problems/remove-outermost-parentheses/
Topic: Stack and Queues
Difficulty: Easy

Approach:
- Init empty stack and result list
- Iterate over each character in the input string
- If stack is empty, push the '(' onto stack and skip adding it to result (outer opening)
- If char is '(' and stack not empty, append it to result and push onto stack
- If char is ')', append it to result, pop stack, and if stack becomes empty remove the just‑added ')' (outer closing)
- Join the result list into a string and return it

Comments:
- Uses two separate if statements instead of elif, which is harmless but slightly less efficient
- Assumes the input string is a valid parentheses sequence; the index from enumerate is unused

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stck = []
        res = []
        for i,char in enumerate(s):
            if not stck:
                stck.append(char)
            else:
                if char == "(":
                    res.append(char)
                    stck.append(char)
                if char == ")":
                    res.append(char)
                    stck.pop()
                    if not stck:
                        res.pop()
        return ''.join(res)

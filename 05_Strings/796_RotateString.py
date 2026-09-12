"""
Problem: Rotate String
LeetCode: https://leetcode.com/problems/rotate-string/
Topic: Strings
Difficulty: Easy

Approach:
- Check if lengths differ and return false
- If strings are empty return true
- Gather indices i where s[i]==goal[0]
- For each start index, walk through goal comparing s[(start+offset)%len(s)] to goal[offset]; if all match return true
- Return false after all candidates fail

Comments:
- Worst‑case time is O(n²) because each matching start may scan the whole string
- Extra space O(n) for the list of candidate start positions

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        starts = []
        if len(s)!=len(goal):
            return False
        if not s:
            return True
        for i,char in enumerate(s):
            if char == goal[0]:
                starts.append(i)
        for start in starts:
            x = start
            for i in range(len(goal)):
                if i == len(goal) - 1 and s[x] == goal[i]:
                    return True
                if s[x] != goal[i]:
                    break
                x = (x+1)%len(s)
        return False

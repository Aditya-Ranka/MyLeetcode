/*
Problem: Valid Parentheses
LeetCode: https://leetcode.com/problems/valid-parentheses/
Topic: Stack and Queues
Difficulty: Easy

Approach:
- Push every opening bracket onto a stack.
- On a closing bracket, fail if the stack is empty or its top isn't the matching opener; otherwise pop.
- Valid iff the stack is empty at the end.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
public:
    bool isValid(string s) {
        stack<char> stck;
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                stck.push(c);
            } 
            else {
                if (stck.empty()) return false;
                if ((c == ')' && stck.top() != '(') ||
                    (c == ']' && stck.top() != '[') ||
                    (c == '}' && stck.top() != '{')) {
                    return false;
                }
                stck.pop();
            }
        }
        return stck.empty();
    }
};

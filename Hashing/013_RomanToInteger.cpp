/*
Problem: Roman to Integer
LeetCode: https://leetcode.com/problems/roman-to-integer/description/
Topic: Hash Table, Math, String
Difficulty: Easy

Problem Description:
- Convert a Roman numeral to an integer
- Each Roman numeral has a unique integer value
- Roman numerals can be combined using addition and subtraction rules
- The result must be a valid integer

Approach:
- Create an unordered map (mp) to store the integer values of each Roman numeral
- Iterate over the input string, checking if the current numeral's value is less than the next one
- If the current numeral's value is less than the next one, subtract its value from the result (using mp[s[i]] and mp[s[i + 1]])
- Otherwise, add its value to the result

Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> mp = {
            {'I', 1}, {'V', 5}, {'X', 10},
            {'L', 50}, {'C', 100},
            {'D', 500}, {'M', 1000}
        };
        
        int result = 0;
        
        for(int i = 0; i < s.length(); i++) {
            if(i + 1 < s.length() && mp[s[i]] < mp[s[i + 1]]) {
                result -= mp[s[i]];
            } else {
                result += mp[s[i]];
            }
        }
        
        return result;
    }
};

/*
Problem: Valid Anagram
LeetCode: https://leetcode.com/problems/valid-anagram/description/
Topic: Hashing
Difficulty: Easy

Approach:
- Use unordered_maps with key being the letter and value being the reptitions of the letter and then compare the two maps. 


Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution {
public:
    bool isAnagram(string s, string t) {
        
        int len1 = s.size();
        int len2 = t.length();
        if (len1!=len2) return false;
        unordered_map<char , int> mp1;
        unordered_map<char , int> mp2;
        for (int i = 0; i < len1; i++){
            mp1[s[i]]++;
            mp2[t[i]]++;
        }
        return mp1==mp2;
    }
};

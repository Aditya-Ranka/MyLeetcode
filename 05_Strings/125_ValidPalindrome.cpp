/*
Problem: Valid Palindrome
LeetCode: https://leetcode.com/problems/valid-palindrome/description/
Topic: Two Pointers
Difficulty: Easy

Approach:
- First we clean the string using a fn we define
- basically check a palindormw normally



Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
    string clean(string s) {
    string res;
    for (char c : s) {
        if (isalpha(c)) {              
            res += tolower(c);         
        }
        if(isdigit(c)){
            res+=c;
        }
    }
    return res;
}

public:
    bool isPalindrome(string s) {
        string x = clean(s);
        for(int i = 0; i < x.size()/2; i++){
            if(x[i]!=x[x.size()-i-1]){
                return false;
            }
        }
        return true;
    }
};

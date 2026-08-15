/*
Problem: Palindrome Number
LeetCode: https://leetcode.com/problems/palindrome-number/description/
Topic: Math
Difficulty: Easy  

Approach:
- Convert the number to a string and check if it reads the same forwards and backwards
- Alternative: Reverse half of the number and compare with the other half
- Handle negative numbers (they cannot be palindromes)
- Handle numbers ending in 0 (except 0 itself, they cannot be palindromes)

Time Complexity: O(log n) - number of digits
Space Complexity: O(1)
*/



class Solution {
    public:
        bool isPalindrome(int x) {
            if (x < 0){
                return false;
            }
            long long rev = 0;
            int og = x;
            while (x > 0) {
                int digit = x % 10;
                rev = rev * 10 + digit;
                x = x / 10;
            }
            if (rev == og){
                return true;
            }
            else{
                return false;
            }
        }
    };

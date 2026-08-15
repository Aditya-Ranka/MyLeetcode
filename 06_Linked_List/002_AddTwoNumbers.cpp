/*
Problem: Add Two Numbers
LeetCode: https://leetcode.com/problems/add-two-numbers/
Topic: Linked List
Difficulty: Medium

Approach:
- Elementary-school addition over two linked lists, digit by digit, carrying as you go.
- Use a dummy head so the first node needs no special case; `tail` tracks the last appended node.
- Loop while either list has nodes OR carry != 0; take each digit (0 if a list is exhausted), sum = x + y + carry.
- Store sum%10 in a new node, carry = sum/10; return dummy->next.

Time Complexity: O(max(m, n))
Space Complexity: O(max(m, n)) for the result list
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode* dummy = new ListNode;
        ListNode* tail = dummy;
        while(l1 || l2 || carry != 0){
            int x = 0;
            int y = 0;
            if(l1){
                x = l1->val;
                l1 = l1->next;
            }
            if(l2){
                y = l2->val;
                l2 = l2->next;
            }
            int sum = x + y + carry;
            carry = sum/10;
            tail->next = new ListNode(sum%10);
            tail = tail->next;
        }
        return dummy->next;
    }
};

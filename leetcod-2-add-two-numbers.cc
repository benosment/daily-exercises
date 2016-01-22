#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *answer = NULL;
        ListNode *head = NULL;
        ListNode *l = NULL;
        bool carry = false;
        int val;

        while (l1 || l2) {
            if (l1 && l2) {
                val = l1->val + l2->val;
            } else if (l1) {
                val = l1->val;
            } else {
                val = l2->val;
            }

            if (carry) {
                val += 1;
            }

            if (val >= 10) {
                val = val % 10;
                carry = true;
            } else {
                carry = false;
            }

            l = new ListNode(val);
            if (answer == NULL) {
                answer = l;
                head = answer;
            } else {
                head->next = l;
                head = head->next;
            }

            if (l1)
                l1 = l1->next;

            if (l2)
                l2 = l2->next;
        }

        if (carry) {
            l = new ListNode(1);
            head->next = l;
            head = head->next;
        }

        return answer;
    }
};


int main() {
    ListNode *l1;
    ListNode *l2;
    ListNode *head;
    ListNode *n;
    Solution s;

    n = new ListNode(3);
    head = n;
    n = new ListNode(4);
    n->next = head;
    head = n;
    n = new ListNode(2);
    n->next = head;
    l1 = n;

    n = new ListNode(4);
    head = n;
    n = new ListNode(6);
    n->next = head;
    head = n;
    n = new ListNode(5);
    n->next = head;
    l2 = n;

    s.addTwoNumbers(l1, l2);
    // while (sol)  {
    //     cout << sol.val << endl;
    // }
}

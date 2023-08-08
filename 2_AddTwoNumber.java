/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode curr1 = l1;
        ListNode curr2 = l2;
        int total = 0;
        int increment = 1;
        while (curr1.next != null && curr2.next != null) {
            total += (curr1.val + curr2.val) * increment;
            increment = increment * 10;
            curr1 = curr1.next;
            curr2 = curr2.next;
        }

        int length = 0;
        int temp = 1;
        while (temp <= total) {
            temp *= 10;
            length += 1;
        }

        while (length > 0) {
            List newCurr = newNode(total / length, newCurr);
            length /= 10;
        }

    }

    public ListNode newNode(int val, ListNode next) {
        ListNode node = new ListNode(val, next);
    }
}
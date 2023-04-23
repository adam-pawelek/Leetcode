# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        add_to_next = 0
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            add_to_next = (l1.val + l2.val) // 10
            head = ListNode((l1.val + l2.val) % 10)
            l1 = l1.next
            l2 = l2.next

        current_node = head
        while (l1 != None and l2 != None):
            current_node.next = ListNode((l1.val + l2.val + add_to_next) % 10)
            add_to_next = (l1.val + l2.val + add_to_next) // 10
            current_node = current_node.next
            l1 = l1.next
            l2 = l2.next

        common_list = None
        if l1 != None:
            common_list = l1
        elif l2 != None:
            common_list = l2

        while common_list != None:
            current_node.next = ListNode((common_list.val + add_to_next) % 10)
            add_to_next = (common_list.val + add_to_next) // 10
            current_node = current_node.next
            common_list = common_list.next

        if add_to_next == 1:
            current_node.next = ListNode(1)

        return head
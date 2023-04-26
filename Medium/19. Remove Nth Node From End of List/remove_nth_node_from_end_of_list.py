# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count_nodes_in_list(self,head,n):
        current_node = head 
        count_nodes = 0
        while (current_node != None):
            current_node = current_node.next
            count_nodes +=1 
        return count_nodes

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  
        count_nodes = self.count_nodes_in_list(head,n)
        if count_nodes == n:
            return head.next
        
        start = ListNode(-1, head)
        current_node = head
        previous_node = start
        for i in range(count_nodes - n):
            previous_node = current_node
            if current_node:
                current_node = current_node.next
            else:
                current_node = None
        
        previous_node.next = current_node.next if current_node else None
        return head
        
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import queue

class Queue_Elements:
    def __init__(self, value, queue_number, node):
        self.value = value
        self.queue_number = queue_number
        self.node = node

    def __lt__(self, other):
        return self.value < other.value


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        all_null = True
        for i in lists:
            if i != None:
                all_null = False
        if all_null == True:
            return None

        head = ListNode()
        result = head

        pque = queue.PriorityQueue()
        for i in range(len(lists)):
            if lists[i] != None:
                help_put = Queue_Elements(lists[i].val, i, lists[i])
                pque.put(help_put)

        while (not pque.empty()):
            element = pque.get()
            lists[element.queue_number] = element.node.next
            if element.node.next:
                help_put = Queue_Elements(element.node.next.val, element.queue_number, element.node.next)
                pque.put(help_put)
            result.next = element.node
            result = element.node
            result.next = None

        return head.next
# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# tags: Linked List Two Pointers


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import deque

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return None

        bufferQ = deque()
        count = 0
        tempNode = head
        while tempNode:
            if count == n + 1:
                bufferQ.popleft()
                count -= 1
            bufferQ.append(tempNode)
            count += 1
            tempNode = tempNode.next

        if len(bufferQ) > n:
            beforeN = bufferQ.popleft()            
            nodeN = bufferQ.popleft()
            beforeN.next = nodeN.next
        else:
            head = head.next
        return head

solution = Solution()
testHead = ListNode(1)
testHead.next = ListNode(2)
testResult = solution.removeNthFromEnd(testHead,1)
print testResult.val
#print testResult.next.val


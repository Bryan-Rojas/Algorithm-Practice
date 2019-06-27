# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(self, head: ListNode) -> ListNode:
    previousNode = None
    currentNode = head
    
    while currentNode:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
        
    return previousNode
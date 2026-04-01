# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        grpprev=dummy

        while True:
            kth=self.getkth(grpprev,k)

            if not kth:
                break
            
            grpnext=kth.next
            prev=grpnext
            curr=grpprev.next
            #reversing

            while curr!=grpnext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp

            tmp=grpprev.next
            grpprev.next=kth
            grpprev=tmp

        return dummy.next
        
    def getkth(self,node,k):
        while node and k>0:
            node=node.next
            k-=1
        return node
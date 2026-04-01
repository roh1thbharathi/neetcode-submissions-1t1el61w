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

            #reverse
            prev=grpnext                  #instead of None next grp first element
            curr=grpprev.next
            while curr!=grpnext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            
            tmp=grpprev.next
            grpprev.next=kth                #kth becomes the first in the grp after reversal
            grpprev=tmp                     #update grpprev to the last node for the next iteration
        return dummy.next

    def getkth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
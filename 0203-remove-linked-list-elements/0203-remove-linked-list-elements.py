# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''lst=[]
        cur=head
        
        while cur!=None:
            lst.append(cur.val)
            cur=cur.next
            
        lst = [num for num in lst if num != val]
                
        dummy=ListNode(0)
        cur=dummy
        
        for num in lst:
            cur.next=ListNode(num)
            cur=cur.next
        return dummy.next'''
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next
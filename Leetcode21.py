
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeList(self, link1: ListNode,link2:ListNode) -> ListNode:
        head = ListNode(-1)
        cur = head
         
        while link1 and link2:
            if link1.val <= link2.val :
                cur.next = link1
                link1 = link1.next
            else :
                cur.next = link2
                link2 = link2.next
            cur = cur.next
        
        if link1!=None:
            cur.next=link1
        
        else:
            cur.next=link2 

        return head.next
    def mergeList2(self, link1: ListNode,link2:ListNode) -> ListNode:
        if not link1 or link2 and link1.val > link2.val:
            link1,link2 = link2,link1
        if link1:
            link1.next = self.mergeList2(link1.next,link2)
        return link1



if __name__=="__main__":
    solution = Solution()

    link1 = ListNode(1,ListNode(2, ListNode(2, ListNode(3, None))))
    link2 = ListNode(1,ListNode(3, ListNode(4, ListNode(5, None))))
    result = solution.mergeList(link1,link2)
    while result:
        print(result.val)
        result = result.next

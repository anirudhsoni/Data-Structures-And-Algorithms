"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OldToNew={None:None}
        old=head
        while old:
            copy=Node(old.val)
            OldToNew[old]=copy
            old=old.next
        old=head
        while old:
            OldToNew[old].next=OldToNew[old.next]
            OldToNew[old].random=OldToNew[old.random]
            old=old.next
        return OldToNew[head]



        
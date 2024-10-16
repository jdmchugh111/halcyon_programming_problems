# Admittedly, I didn't have much experience with linked lists before solving this so I did a little bit of research.
# Upon researching it seems like Rust would actually be optimal for solving something like this since it has built in LinkedList struct you can use.
# This solution works when I run it, but I'm not sure if it's optimized. 
# The if/else conditional nested inside of the while block seems like it could be refactored, but I'm not sure what a better alternative would be.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(list):
    head = ListNode(0)
    curr = head
    total = 0
    node = list.next

    while node:
        if node.val == 0:
            curr.next = ListNode(total)
            curr = curr.next
            total = 0
        else:
            total += node.val
        node = node.next

    return head.next


# I know this wasn't part of the prompt, but I wanted to check my work by printing out the modified linked list

linked_list = ListNode(0, ListNode(1, ListNode(2, ListNode(0, ListNode(3, ListNode(4, ListNode(0)))))))
new_linked_list = mergeNodes(linked_list)

def printList(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

printList(linked_list)
printList(new_linked_list)
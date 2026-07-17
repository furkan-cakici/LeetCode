from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next

def list_to_linkedlist(elements: list) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for el in elements:
        current.next = ListNode(el)
        current = current.next
    return dummy.next

def linkedlist_to_list(node: Optional[ListNode]) -> list:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    solution = Solution()

    l1_ex1 = list_to_linkedlist([2, 4, 3])
    l2_ex1 = list_to_linkedlist([5, 6, 4])
    result_node_1 = solution.addTwoNumbers(l1_ex1, l2_ex1)
    print(f"Örnek 1 Sonucu: {linkedlist_to_list(result_node_1)} | Beklenen: [7, 0, 8]")

    l1_ex2 = list_to_linkedlist([0])
    l2_ex2 = list_to_linkedlist([0])
    result_node_2 = solution.addTwoNumbers(l1_ex2, l2_ex2)
    print(f"Örnek 2 Sonucu: {linkedlist_to_list(result_node_2)} | Beklenen: [0]")

    l1_ex3 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
    l2_ex3 = list_to_linkedlist([9, 9, 9, 9])
    result_node_3 = solution.addTwoNumbers(l1_ex3, l2_ex3)
    print(f"Örnek 3 Sonucu: {linkedlist_to_list(result_node_3)} | Beklenen: [8, 9, 9, 9, 0, 0, 0, 1]")

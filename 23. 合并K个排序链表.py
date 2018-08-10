# coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        head = ListNode(None)
        cur_node = head
        heap_list = [lists[i] for i in range(len(lists)) if lists[i]]
        k = len(heap_list)
        if not k:
            return
        # 建立最小堆
        for i in range((k-2)//2, -1, -1):
            self.min_heap_move(heap_list, i, k)

        while len(heap_list):
            temp_node = heap_list[0]
            cur_node.next = temp_node
            cur_node = cur_node.next

            if temp_node.next:
                heap_list[0] = temp_node.next
            else:
                if len(heap_list) == 1:
                    break
                heap_list[0] = heap_list.pop(-1)
            self.min_heap_move(heap_list, 0, len(heap_list))
        return head.next


    def min_heap_move(self, heap, root, heapsize):
        if root >= heapsize:
            return
        left = 2 * root + 1
        right = 2 * root + 2
        small = root
        print heap[small], left, heapsize
        if left < heapsize and heap[left].val < heap[small].val:
            small = left
        if right < heapsize and heap[right].val < heap[small].val:
            small = right
        if small != root:
            heap[small], heap[root] = heap[root], heap[small]
            self.min_heap_move(heap, small, heapsize)
a0 = ListNode(1)
a1 = ListNode(4)
a2 = ListNode(5)
a3 = ListNode(1)
a4 = ListNode(3)
a5 = ListNode(4)
a6 = ListNode(2)
a7 = ListNode(6)

# 145
a0.next = a1
a1.next = a2
# 134
a3.next = a4
a4.next = a5
# 26
a6.next = a7



t = Solution()
a = t.mergeKLists([[],ListNode(1)])
while a:
    print(a.val)
    a = a.next
# a = [4,1,2]
# t.min_heap_move(a, 0, len(a))
# print(a)

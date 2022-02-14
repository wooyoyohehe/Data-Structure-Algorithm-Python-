# Leetcode

1. Creat an empty of list of length of n

        list_n = [0] * n

2. transfer integer to binary

        s = bin(5)
        s == "0b101"

3. from uppercase to lowercase

        s = "ABC"
        s.lower()

4. from binary to decimal

        d = int('11111111', 2)

5. create a m*n empty 2D list

        x = [[None for _ in range(n)] for _ in range(m)]

6. infinite in python

        a = float('inf')

7. 

        preorder traverse: root -> left -> right
        inorder traverse: left -> root -> right
        postorder traverse: left -> right -> root

8. backtrack

        result = []
        def backtrack(路径, 选择列表):
        if 满足结束条件:
                result.add(路径)
                return
        
        for 选择 in 选择列表:
                做选择
                backtrack(路径, 选择列表)
                撤销选择

9. find the index of an item in the list
        ["foo", "bar", "baz"].index("bar")

10. 
        reverse a singly linked list
                <!-- this step is really important or you will get only last two nodes -->
                prev = None 
                cur = head
                while cur:
                        next = cur.next
                        cur.next = prev
                        prev = cur
                        cur = next
                return prev

11. delete a node in the linked list
        prev.next.next = prev.next

12. convertion between letter and ascii
        a = 'a'
        ascii_of_a = ord(a)
        letter_a = chr(97)

13. convert a word to a list of chars
        list(s)

14. 
        PriorityQueue
                from queue import PriorityQueue
                q = PriorityQueue()
                q.put([priority, "sth"])
                q.get()
                q.empty()
                q.qsize()

15. 
        heapq
                q = []
                heapq.heappush(q, (priority, value))
                heapq.heappop(q)
                heapq.heapreplace(heap, val)：先进行pop，在进行push。
                heapq.heappushpop(heap, val)：先进行push，再进行pop，返回pop后的值。
                使用replace、pushpop要比，使用一遍push再使用pop要快。
                heapq.nlargest(n, heap)：查找堆中最大的n个元素
                heapq.nsmallest(n, heap)：查找堆中最小的n个元素

                build heap: O(n)
                heapsort: O(nlogn)

16. 
        Situation：事情是在什么情况下发生
        Task：你是如何明确你的任务的
        Action：针对这样的情况分析，你采用了什么行动方式
        Result：结果怎样，在这样的情况下你学习到了什么




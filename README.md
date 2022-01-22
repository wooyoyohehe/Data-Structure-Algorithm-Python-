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

10. reverse a singly linked list
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
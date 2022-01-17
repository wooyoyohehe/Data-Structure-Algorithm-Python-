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
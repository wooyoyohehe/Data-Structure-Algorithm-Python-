class MyStack(object):

    def __init__(self):
        self.q1 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        
        

    def pop(self):
        """
        :rtype: int
        """
        return(self.q1.pop())
        

    def top(self):
        """
        :rtype: int
        """
        return self.q1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.q1) == 0:
            return True
        else:
            return False
        
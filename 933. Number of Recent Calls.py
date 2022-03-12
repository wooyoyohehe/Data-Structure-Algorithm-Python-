class RecentCounter(object):

    def __init__(self):
        self.requests = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        while self.requests[0] < t-3000:
            self.requests.pop(0)
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
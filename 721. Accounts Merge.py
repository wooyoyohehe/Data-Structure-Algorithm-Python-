class DSU():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i,j):
        self.parent[self.find(i)] = self.find(j)
        
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        mails = {}
        index = 0
        dsu = DSU(10000)
        dic = {}
        for account in accounts:
            if account[0] not in dic:
                dic[account[0]] = set()
            for i in range(1, len(account)):
                dic[account[0]].add(account[i])
                if account[i] not in mails:
                    mails[account[i]] = index
                    index += 1
                if i > 1:
                    dsu.union(mails[account[i]], mails[account[i-1]])
        ans = []
        for key in dic:
            temp_dic = {}
            for val in dic[key]:
                if dsu.find(mails[val]) not in temp_dic:
                    temp_dic[dsu.find(mails[val])] = []
                temp_dic[dsu.find(mails[val])].append(val)
            for key1 in temp_dic:
                ans.append([key]+sorted(temp_dic[key1]))
        return ans
                    
        

                
                
        
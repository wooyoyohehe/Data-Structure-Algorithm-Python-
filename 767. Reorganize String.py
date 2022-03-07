class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for letter in s:
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter] += 1
        if max(dic.values()) > (len(s)+1)//2:
            return ""
        q = []
        for key in dic:
            heapq.heappush(q, [-dic[key], key])
        ans = ""
        while q:
            count1, letter1 = heapq.heappop(q)
            ans += letter1
            if q:
                count2, letter2 = heapq.heappop(q)
                ans += letter2
                if count2 < -1:
                    heapq.heappush(q, [count2+1, letter2])
            if count1 < -1:
                heapq.heappush(q, [count1+1, letter1])
        return ans
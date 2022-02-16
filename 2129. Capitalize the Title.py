class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title = title.split(" ")
        for i in range(len(title)):
            title[i] = title[i].lower()
            if len(title[i]) > 2:
                title[i] = chr(ord(title[i][0])-32)+title[i][1:]
        return " ".join(title)
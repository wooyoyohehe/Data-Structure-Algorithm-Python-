class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        day,mon,year = date.split(" ")
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        if month.index(mon) < 9:
            mon = "0" + str(month.index(mon)+1)
        else:
            mon = str(month.index(mon)+1)
        day = day[:-2]
        if len(day) == 1:
            day = "0" + day
        return year + "-" + mon + "-" + day
            
        
        
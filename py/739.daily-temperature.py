class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if not temperatures:
            return []
        res = [0]
        highest = [(temperatures[-1], 1)]
        for i in range(2, len(temperatures) + 1):
            while highest and temperatures[-i] >= highest[-1][0]:
                highest.pop()
            if not highest:
                highest = [(temperatures[-i], i)]
                res.append(0)
            else:
                res.append(i - highest[-1][1])
                highest.append((temperatures[-i], i))
        return res[-1::-1]
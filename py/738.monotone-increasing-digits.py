class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def help(d, l):
            for i in l:
                if i > d:
                    return True
                if i == d:
                    continue
                if i < d:
                    return False
            return True
        n = []
        while N:
            n.append(N % 10)
            N /= 10
        n.reverse()
        res = [9] * len(n)

        for i, d in enumerate(n):
            if help(d, n[i:]):
                res[i] = d
            else:
                res[i] = d - 1
                break
        
        r = 0
        for i in res:
            r *= 10
            r += i
        return r
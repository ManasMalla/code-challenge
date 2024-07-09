class Solution:
    def print2largest(self, arr):
        a = 0
        b = -1
        if len(arr) <= 1:
            return -1
        for c in arr:
            if c > a:
                b = a
                a = c
            elif c > b and c != a :
                b = c
        return b

class Solution:
    def largest(self, n : int, arr : List[int]) -> int:
        a = 0
        for i in arr:
            if a < i:
                a = i
        return a
        # code here

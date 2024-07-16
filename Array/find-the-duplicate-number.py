class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if not d.get(i,0):
                d[i]=1
            else:
                return i

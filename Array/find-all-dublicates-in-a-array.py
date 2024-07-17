class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s=set()
        dub=set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                dub.add(i)
        return dub

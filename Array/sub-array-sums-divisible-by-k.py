class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        count=0
        running_sum=0
        for i in nums:
            running_sum+=i
            rem= running_sum%k
            if rem in d:
                count+=d[rem]
                d[rem]+=1
            else:
                d[rem]=1
        return count 

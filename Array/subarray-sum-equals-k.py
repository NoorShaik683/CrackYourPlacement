class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #bruteforce
        # c=0
        # for i in range(len(nums)):
        #     curr_sum=0
        #     for j in range(i, len(nums)):
        #         curr_sum+=nums[j]
        #         if curr_sum==k:
        #             c+=1
        # return c

        d={0:1}
        c=0
        curr_sum = 0
        for i in nums:
            curr_sum+=i
            temp = curr_sum-k
            if d.get(temp):
                c+=d[temp]
            d[curr_sum]=d.get(curr_sum,0)+1
        return c

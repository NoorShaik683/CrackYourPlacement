class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        final=set()
        nums.sort()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            end = n-1
            while left<end:
                s=nums[i]+nums[left]+nums[end]
                if s==0:
                    final.add((nums[i],nums[left],nums[end]))
                    while left<end and nums[left]==nums[left+1]:
                        left+=1
                    while left<end and nums[end]==nums[end-1]:
                        end-=1
                    left+=1
                    end-=1
                elif s<0:
                    left+=1
                else:
                    end-=1
        return final
        

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=0
        x=len(nums)
        end=x-1 
        while(start<=end):
            mid=(start+end)//2
            if target==nums[mid]:
                start=mid
                end=mid
                while start>=0 and nums[start]==target:
                    start-=1
                while end<=x-1 and nums[end]==target:
                    end+=1
                return [start+1,end-1]    
            elif target<nums[mid]:
                end=mid-1
            else:
                start=mid+1
        return [-1,-1]   

        
        
            
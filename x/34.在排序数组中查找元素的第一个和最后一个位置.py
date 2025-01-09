class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(target:int) -> int:
            left,right=0,len(nums)
            while left<right:
                mid=left+(right-left)//2
                if nums[mid]>target:
                    right=mid
                else:
                    left=mid+1
            return right
        start=search(target-1)
        if start==len(nums) or nums[start]!=target:
            return [-1,-1]
        end=search(target)
        return [start, end - 1]
        
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = left_max = right_max = 0
        for i in range(len(height)):
            left_max = max(height[i], left_max)
            right_max = max(height[-i-1], right_max)
            ans += left_max + right_max - height[i]
        return ans - left_max * len(height)
        
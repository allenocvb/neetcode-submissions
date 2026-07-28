class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            smaller_height = min(heights[l], heights[r])
            current_area = smaller_height * width
            max_area = max(max_area, current_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
        
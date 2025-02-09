class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_value = 0
        right_value = len(height) - 1
        max_area = 0
        
        while left_value < right_value:
            width = right_value - left_value
            height_of_container = min(height[left_value], height[right_value])
            area = width * height_of_container
            max_area = max(max_area, area)
            
            if height[left_value] < height[right_value]:
                left_value += 1
            else:
                right_value -= 1
        
        return max_area
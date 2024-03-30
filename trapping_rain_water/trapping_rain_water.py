"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105"""

def trap(height: list[int]) -> int:
    if not height: return 0
    
    left_pointer, right_pointer = 0, len(height)-1
    maximum_left, maximum_right = height[left_pointer], height[right_pointer]
    area:int = 0

    while left_pointer < right_pointer:
        if maximum_left < maximum_right:
            left_pointer += 1
            maximum_left = max(maximum_left, height[left_pointer])
            area += maximum_left - height[left_pointer]
        
        else:
            right_pointer -=1
            maximum_right = max(maximum_right, height[right_pointer])
            area += maximum_right - height[right_pointer]
        
    return area    

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))
print(trap([2,0,2]))
print(trap([4,2,0,3,2,5]))
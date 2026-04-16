class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left = []
        leftmax = height[0]
        for i in range(len(height)):
            left.append(leftmax)
            leftmax = max(leftmax, height[i])
        
        right = []
        rightmax = height[len(height) - 1]
        for i in range(len(height) - 1, -1, -1):
            right.append(rightmax)
            rightmax = max(rightmax, height[i])
        
        rev = right[::-1]
        
        trapped = 0
        for i in range(0, len(height)):
            val = min(left[i], rev[i])
            if val > height[i]:
                trapped += val - height[i]
        return trapped
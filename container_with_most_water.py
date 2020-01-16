class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        head = 0
        tail = len(height)-1
        for i in range(len(height)):
            width = tail - head
            if height[head] > height[tail]:
                temp = width * height[tail]
                tail -=1
            else:
                temp = width * height[head]
                head+=1
            if temp > water:
                water = temp
        return water
            
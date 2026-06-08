#Problem: Second Largest Element in Array
#Platform: Geeks For Geeks
#Idea: Track largest and second largest while iterating once
#Time complexity: O(n)
#Space complexity: O(1)

class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        second_largest = -1
        
        for x in arr:
            if x > largest:
                second_largest = largest
                largest = x
            elif x < largest and x > second_largest:
                second_largest = x
        return second_largest
      
arr = [10, 5, 8, 20, 15]

obj = Solution()
result = obj.getSecondLargest(arr)

print("Second largest element is:", result)

# Problem: Move all zeroes to the end of array
# Idea: Shift non-zero elements to front, fill rest with zeroes
# Time Complexity: O(n)
# Space Complexity: O(1)

Code:
class Solution:
    def pushZerosToEnd(self, arr):
        
        # Count non-zero and zero elements
        non_zero_count = 0
        zero_count = 0
        
        for x in arr:
            if x == 0:
                zero_count += 1
            else:
                non_zero_count += 1
        
        print("Non-zero count:", non_zero_count)
        print("Zero count:", zero_count)
        
        # Move non-zero elements forward
        j = 0
        
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[j] = arr[i]
                j += 1
        
        # Fill remaining positions with zero
        for i in range(j, len(arr)):
            arr[i] = 0
        
        return arr
arr = [1, 2, 0, 4, 3, 0, 5, 0]

obj = Solution()
result = obj.pushZerosToEnd(arr)

print(result)

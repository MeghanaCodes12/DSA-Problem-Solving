#Problem: Moving zeroes to an end in Array
#Platform: Geeks For Geeks
#Idea: Shift non-zero elements to front, fill rest with zeroes.
#Time complexity: O(n)
#Space complexity: O(1)

Code:
class Solution:
	def pushZerosToEnd(self, arr):
	    
	    #Lets count the elements
	    non_zero_count = 0
	    zero_count = 0
	    
	    for x in arr:
	        if x==0:
	            zero_count += 1
	        else:
	            non_zero_count += 1
	    print("Non-zero elements count:" , non_zero_count)
	    print("Zero elements count:" , zero_count)
	    
	    #Lets move the non-zeroes to the front
	    j=0
	    
	    for i in range(len(arr)):
	        if arr[i]!=0:
	            arr[j] = arr[i]
	            j = j+1
	   
	    #Lets move the zeroes to the end
	    for i in range(j, len(arr)):
	        arr[i] = 0
	        
	    return arr 
	    
arr = [ 1,2,4,0,7,0,5,0,9]
sol = Solution()
result = sol.pushZerosToEnd(arr)

print(result)

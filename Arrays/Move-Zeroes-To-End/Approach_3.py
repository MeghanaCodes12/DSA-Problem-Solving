// Problem: Move all zeroes to the end of the array
// Platform: GeeksforGeeks
// Idea: Use two-pointer approach to place non-zero elements at the front
// Approach: Swap non-zero elements with the position of first zero encountered
// Technique: In-place swapping using a count pointer (Two Pointers)
// Time Complexity: O(n)
// Space Complexity: O(1)

function pushZerosToEnd(arr) {
    
    // Pointer to track the position
    // for next non-zero element
    let count = 0;
    
    for (let i = 0; i < arr.length; i++) {
        
        // If the current element is non-zero
        if (arr[i] !== 0) {
            
            // Swap the current element
            // with the 0 at index 'count'
            [arr[i], arr[count]] = [arr[count], arr[i]];
            
            // Move 'count' pointer to the next position
            count++;
        }
    }
}

// Driver code 
const arr = [1, 2, 0, 4, 3, 0, 5, 0];
pushZerosToEnd(arr);
console.log(arr.join(" "));

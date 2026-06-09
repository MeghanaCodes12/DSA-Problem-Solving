// Problem: Move all zeroes to the end of the array
// Platform: GeeksforGeeks
// Idea: Store all non-zero elements first, then fill remaining positions with zeroes
// Approach: Use a temporary array to maintain order of non-zero elements
// Time Complexity: O(n)
// Space Complexity: O(n)

function pushZerosToEnd(arr)
{
    const n = arr.length;
    const temp = new Array(n);

    // to keep track of the index in temp[]
    let j = 0;

    // Copy non-zero elements to temp[]
    for (let i = 0; i < n; i++) {
        if (arr[i] !== 0) {
            temp[j++] = arr[i];
        }
    }

    // Fill remaining positions in temp[] with zeros
    while (j < n)
        temp[j++] = 0;

    // Copy all the elements from temp[] to arr[]
    for (let i = 0; i < n; i++)
        arr[i] = temp[i];
}

// Driver Code
const arr = [1, 2, 0, 4, 3, 0, 5, 0];
pushZerosToEnd(arr);

console.log(arr.join(" "));

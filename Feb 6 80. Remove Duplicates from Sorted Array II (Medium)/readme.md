# [Python 3] 👆 Two Pointer Solution👇

## 1️⃣ Two Pointer Explained:
We init **left pointer** and **count** = 1, and move **right pointer** through the nums
> 1. If we see nums[right] == nums[right - 1]=> count += 1 else: count = 1.    This allow us to keep track number of duplicates remain under 2
> 2. We move right number to left while count <= 2 because once count > 2 means we find duplicates need to remove so we move only right

## Complexity Analysis
* Time: O(N) : Let *N* be the length of nums
* Space: O(1) 

## Code

See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/38e1c16fcbc6ee036134631a35cbfc1c9b972d33/Feb%206%2080.%20Remove%20Duplicates%20from%20Sorted%20Array%20II%20(Medium)/Solution.py#L1)

## 2️⃣ Alternative Solution
Since we have to keep update left pointer, means we update leftpointer by number of count
Which we can consider a length of dupilcate sequence, once length <= 1 or nums[length - 2] != val means we find not duplicate num so we update length and length index


## Code

See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/38e1c16fcbc6ee036134631a35cbfc1c9b972d33/Feb%206%2080.%20Remove%20Duplicates%20from%20Sorted%20Array%20II%20(Medium)/Solution.py#L14)


# [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

## Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
## Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

# todo
## [409. Longest Palindrome (Easy)](https://leetcode.com/problems/longest-palindrome/description/)
基于中心点枚举法 Enumeration
基于动态规划 Dynamic Programming

## [Implement strStr](http://www.lintcode.com/problem/strstr/)

# Binary Search & LogN Algorithm
比O(n)更优的时间复杂度几乎只能是O(logn)的二分法
二分法模板: start + 1 < end; start + (end - start) / 2; A[mid] ==, >, <; A[start] A[end] ? target

## [704. Binary Search (Easy)](https://leetcode.com/problems/binary-search/description/)
[lintcode's version](https://www.lintcode.com/problem/classical-binary-search/description)
```html
Find any position of a target number in a sorted array. Return -1 if target does not exist.

Example
Given [1, 2, 2, 4, 5, 5].

For target = 2, return 1 or 2.

For target = 5, return 4 or 5.

For target = 6, return -1.

Challenge
O(logn) time
```
总结：背好模板，lintcode 的 test case 包含空输入数组，需要 python3 的 // 整除运算符才能过
```python
class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if (len(nums) == 0):
          return -1
        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) // 2     
            if (nums[mid] == target):
                return mid
            elif (target > nums[mid]):
                start = mid
            else:
                end = mid    
        if (nums[start] == target):
            return start
        if (nums[end] == target):
            return end
        return -1

```

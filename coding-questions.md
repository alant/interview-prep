# todo
## [409. Longest Palindrome (Easy)](https://leetcode.com/problems/longest-palindrome/description/)
基于中心点枚举法 Enumeration
基于动态规划 Dynamic Programming

## [Implement strStr](http://www.lintcode.com/problem/strstr/)

# Binary Search & LogN Algorithm
比O(n)更优的时间复杂度几乎只能是O(logn)的二分法
二分法模板: start + 1 < end; start + (end - start) / 2; A[mid] ==, <, >; A[start] A[end] ? target

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
            elif (nums[mid] < target):
                start = mid
            else:
                end = mid    
        if (nums[start] == target):
            return start
        if (nums[end] == target):
            return end
        return -1

```
总结：背好模板，lintcode 的 test case 包含空输入数组，需要 python3 的 // 整除运算符才能过

## [lintcode 14. First Position of Target (Easy)](https://www.lintcode.com/problem/first-position-of-target/description)
```html
Description
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Have you met this question in a real interview?  
Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

Challenge
If the count of numbers is bigger than 2^32, can your code work properly?
```
思路：找到了不要 return，扔掉大的一半，继续找
```python
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if (len(nums) == 0):
            return -1
        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if (nums[mid] >= target):
                end = mid
            elif (nums[mid] < target):
                start = mid
        if (nums[start] == target):
            return start
        if (nums[end] == target):
            return end
        return -1
```
总结：背好模板，模板 v5

## [278. First Bad Version (Easy)](https://leetcode.com/problems/first-bad-version/description/)
```html
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
```
思路：前面 first position of target 的变体，可以不做

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 0, n
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if (isBadVersion(mid)):
                end = mid
            else:
                start = mid
        if (isBadVersion(start)):
            return start
        if (isBadVersion(end)):
            return end
        return -1
```
总结：可不做

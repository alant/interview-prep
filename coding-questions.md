# todo
### [658. Find K Closest Elements (Medium)](https://leetcode.com/problems/find-k-closest-elements/description/)
```html
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
```

### [409. Longest Palindrome (Easy)](https://leetcode.com/problems/longest-palindrome/description/)
```html
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
```

基于中心点枚举法 Enumeration
基于动态规划 Dynamic Programming

### [Implement strStr](http://www.lintcode.com/problem/strstr/)
```html
Description
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Have you met this question in a real interview?  
Clarification
Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.
Example
If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.

Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
```
[240. Search a 2D Matrix II (Medium)](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)
[Lintcode Search a 2D Matrix II](http://www.lintcode.com/en/problem/search-a-2d-matrix-ii/)

### [600. Smallest Rectangle Enclosing Black Pixels (Hard)](https://www.lintcode.com/problem/smallest-rectangle-enclosing-black-pixels/description)
```html
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example
For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.
```
思路：   

### [680. Valid Palindrome II (Easy)](https://leetcode.com/problems/valid-palindrome-ii/description/)
```html
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
```
思路：目前网上看到大部分答案都以贪心算法为主， 等看贪心了再刷这题

# Binary Search & LogN Algorithm
比O(n)更优的时间复杂度几乎只能是O(logn)的二分法
二分法模板: start + 1 < end; start + (end - start) / 2; A[mid] ==, <, >; A[start] A[end] ? target

### [704. Binary Search (Easy)](https://leetcode.com/problems/binary-search/description/)
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

### [Lintcode 14. First Position of Target (Easy)](https://www.lintcode.com/problem/first-position-of-target/description)
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
            else:
                start = mid
        if (nums[start] == target):
            return start
        if (nums[end] == target):
            return end
        return -1
```
总结：背好模板，模板 v5

### [278. First Bad Version (Easy)](https://leetcode.com/problems/first-bad-version/description/)
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

### [Lintcode 460. Find K Closest Elements (Medium)](https://www.lintcode.com/problem/find-k-closest-elements/description)
```html
Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

Example
Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].

Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

Challenge
O(logn + k) time complexity.

Notice
The value k is a non-negative integer and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^4
Absolute value of elements in the array and x will not exceed 10^4
```
思路：二分查找找到 start end 以后，用两个判断条件来限制取值范围。当 left 超过取值范围之后，只取 right 以后的数。
当 right 超过取值范围之后，只取 left 之前的数

```python
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        start, end = 0, len(A) - 1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if (A[mid] < target):
                start = mid
            else:
                end = mid
        left, right = start, end
        result = []
        while (k > 0):
            if (left >= 0 and right <= len(A) - 1):
                if (target - A[left] <= A[right] - target):
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1
            elif (left < 0):
                result.append(A[right])
                right += 1
            else:
                result.append(A[left])
                left -= 1
            k -=  1
        return result

```
总结，一开始没有充分理解题目，题目说的是 k closest elements to x in the array， 找到离 x 最近的点以后要往两边看 k 次。解题方法多少有点需要背的因素。

### [153. Find Minimum in Rotated Sorted Array (Medium)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)
```html
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
```
思路：找 pivot，pivot > 0 时返回 nums[pivot + 1]。找 pivot 时,如果 mid < start, 扔 end， 如果 mid > start 扔 start
```python
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums[0] < nums[len(nums) - 1]):
            return nums[0]
        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if (nums[mid] < nums[start]):
                end = mid
            else:
                start = mid
        return nums[end]
```
总结：应改为 Easy 难度的题。
Follow up: 如果有重复的数? 无法保证在 Log(N) 的时间复杂度内解决 例子:[1,1,1,1,1....,1] 里藏着一个 0.最坏情况下需要把每个位置上的1都看一遍，才能找到最后一个有0 的位置. 考点:能想到这个最坏情况的例子

### [Lintcode 585. Maximum Number in Mountain Sequence (Medium)](https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/description)
[852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/)
```html
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.
Example
Given nums = [1, 2, 4, 8, 6, 3] return 8
Given nums = [10, 9, 8, 7], return 10
```
思路：一开始以为跟上题一样，返回 start 就行了，也许是不值得做的题，可是没有考虑到后面不是递增而是递减。所以，需要改算法为切一刀，判断递增就扔左边，递减就扔右边， 不然就找到了中点
```python
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if (nums[mid - 1] < nums[mid] < nums[mid + 1]):
                start = mid
            elif (nums[mid - 1] > nums[mid] > nums[mid + 1]):
                end = mid
            else:
                return nums[mid]
        return nums[end] if nums[start] < nums[end] else nums[start]
```

### [74. Search a 2D Matrix (Medium)](https://leetcode.com/problems/search-a-2d-matrix/description/)
```html
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```
思路：二分查找，不过是放到二维数组里了
```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        startR, endR = 0, len(matrix) - 1
        startC, endC = 0, len(matrix[0]) - 1
        while(startR + 1 < endR):
            midR = startR + (endR - startR) // 2
            if (matrix[midR][0] == target):
                return True
            elif (matrix[midR][0] < target):
                startR = midR
            else:
                endR = midR
        if (matrix[startR][0] == target or matrix[endR][0] == target):
            return True
        elif (matrix[endR][0] < target):
            targetR = endR
        else:
            targetR = startR
        while(startC + 1 < endC):
            midC = startC + (endC - startC) // 2
            if (matrix[targetR][midC] == target):
                return True
            elif (matrix[targetR][midC] < target):
                startC = midC
            else:
                endC = midC
        if (matrix[targetR][startC] == target or matrix[targetR][endC] == target):
            return True
        return False
```
总结：注意检查空输入

### [Lintcode 61. Search for a Range (Medium)](https://www.lintcode.com/problem/search-for-a-range/description)
```html
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Challenge
O(log n) time.
```
思路：找一个数的第一次和最后一次出现的 index
```python
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        firstO, lastO = -1, -1
        if len(A) == 0:
            return [firstO, lastO]
        start, end = 0, len(A) - 1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if (A[mid] < target):
                start = mid
            else:
                end = mid
        if (A[end] == target):
            firstO = end        
        if (A[start] == target):
            firstO = start
        start, end = 0, len(A) - 1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if (A[mid] <= target):
                start = mid
            else:
                end = mid
        if (A[start] == target):
            lastO = start
        if (A[end] == target):
            lastO = end
        return [firstO, lastO]
```
总结：注意检查空输入！

### [162. Find Peak Element (Medium)](https://leetcode.com/problems/find-peak-element/description/)
```html
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
```
思路：和前面 Lintcode 585. Maximum Number in Mountain Sequence 应该是一个路子
```python
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return -1
        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if (nums[mid - 1] < nums[mid] < nums[mid + 1]):
                start = mid
            elif (nums[mid - 1] < nums[mid] > nums[mid + 1]):
                return mid
            else:
                end = mid
        if nums[start] > nums[end]:
            return start
        else:
            return end
```
总结：确实和前面一样， 不用做

### [33. Search in Rotated Sorted Array (Medium)](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
```html
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```
思路：第一感觉是得知道 pivot 在哪，有 pivot 一侧不能随便扔，但是更优的方法是查单调的侧是否可以扔
```python
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if nums[start] < nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1    
```
总结： 注意 [1, 3, 5] target 为 1 这种边界条件， 判断 target 在单调这边需要加等号

### [Lintcode 140. Fast Power (Medium)](https://www.lintcode.com/problem/fast-power/description)
```html
Calculate the a**n % b where a, b and n are all 32bit integers.

Example
For 2**31 % 3 = 2

For 100**1000 % 1000 = 0

Challenge
O(logn)
```
思路：第一感觉是：需要用某种数学方法，取模只取决于这个数取模后剩下的数加多少次，可以将次方换成乘法，再取模，乘法可以换算成 n 次幂取模 b 再乘 a。
总结：递归版本： (a * b) % p = (a % p * b % p) % p 将 a^n % b 分解为 (a^(n/2) * a^(n/2) * (a)) %b = ((a^(n/2) * a^(n/2))%b * (a)%b) %b = ((a^(n/2)%b * a^(n/2)%b)%b * (a)%b) %b； 非递归版本，思路是转换为二进制

### [50. Pow(x, n) (Medium)](https://leetcode.com/problems/powx-n/description/)
```html
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
```
思路：递归
```python
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.power(x, -n)
        else:
            return self.power(x, n)
    def power(self, x, n):    
        if n == 0:
            return 1
        result = self.power(x, n // 2)
        if n % 2 == 0:
            return result * result
        else:
            return x * result * result
```
总结：有固定写法套路的题目， 不值得做。
# Two pointers
## 预热
### [26. Remove Duplicates from Sorted Array (Easy)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
```html
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```
思路：简单题， 慢指针只有在快指针碰到不同的值才走。
```python
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1
```
总结：纯热身，秒解
### [160. Intersection of Two Linked Lists (Easy)](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)
```html
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
```
思路：统计两条链走到头的长度，lenA 和 lenB, 然后让长的那条先走两者的差值，然后一起走，返回相遇的那点

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        savedHeadA, savedHeadB = headA, headB
        if headA == None or headB == None:
            return None
        lenA, lenB = 1, 1
        while headA.next != None:
            headA = headA.next
            lenA += 1
        while headB.next != None:
            headB = headB.next
            lenB += 1
        if lenA > lenB:
            diff = lenA - lenB
            for x in xrange(diff):
                savedHeadA = savedHeadA.next
        else:
            diff = lenB - lenA
            for x in xrange(diff):
                savedHeadB = savedHeadB.next
        while savedHeadA != None:
            if savedHeadA == savedHeadB:
                return savedHeadA
            else:
                savedHeadA = savedHeadA.next
                savedHeadB = savedHeadB.next
        return None
```
总结：1.注意空输入（不能假设 headA 或 B 有 next）2.注意 headA headB 是一个节点 i.e. 合体的情况
### [141. Linked List Cycle (Easy)](https://leetcode.com/problems/linked-list-cycle/description/)
```html
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
```
思路：记得应该是慢的 +1 快的 +2 如果有 loop 会重逢。。。可能不那么值得做，热身吧
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow, fast = head, head.next.next
        while fast != None and fast.next != None and fast.next.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
```
总结：有点意思，适合热身，代码写好后要测的情况比较多， 1 -> 2 无 loop，1 -> 2 -> 3 -> 4 loop 回 2 这些情况都要测一下。防止 next 和 next.next 不存在的情况
### [142. Linked List Cycle II (Medium)](https://leetcode.com/problems/linked-list-cycle-ii/description/)
```html
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
```
思路：记得好像是找到有 loop 以后走多久能找到 cycle 的起点。
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        slow, fast = head, head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next            
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
        return None
```        
总结：slow fast 同时在 head，先走再判断。不然容易出错。有数学关系，面试当场不一定能推导出来。就算推导出来也要注意前面的 slow，fast写法。
    a            b
A ------ B --------+
         |         |
       c |         |
         +-------- C

* A: 起始点
* B: Cycle Begins
* C: 1st 快慢指针相遇点

* A->B: a
* B->C: b
* C->B: c
* 环的长度 (b+c) 为 R

第一次相遇时，慢指针所走步数为 a + b 快指针走的步数为 *a + b + nR*
我们知道快指针是慢指针速度的2倍，因此 2(a + b) = a + b + nR 那么 a + b = nR
同时 b + c = R 所以 a = (n - 1)R + c;
也就是说，从A点和C点同时出发，以相同的速度前进，相遇的位置将是B。
## 题目
### [283. Move Zeroes (Easy)](https://leetcode.com/problems/move-zeroes/description/)
```html
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
```
思路：第一感觉是快指针直接跑到最后， 慢指针遇到 0 就接快指针面；仔细读题才发现是数组 in place 转换；那就快指针到第一个非 0 的数，直到快指针到最后
```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return
        slow, fast = 0, 0
        while fast < len(nums) and nums[fast] == 0:
            fast += 1
        while slow < len(nums) - 1 and fast < len(nums):
            if nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                while fast < len(nums) and nums[fast] == 0:
                    fast += 1
            slow += 1
            if slow > fast:
                fast += 1
                while fast < len(nums) and nums[fast] == 0:
                    fast += 1
```
总结：思路简单，但是情况很多， 需要考虑，无 0， 0 在前， 后， 中四种情况 [1,2], [0, 1, 2], [1, 0, 0], [1, 0, 0, 1] 才能写对

### [125. Valid Palindrome (Easy)](https://leetcode.com/problems/valid-palindrome/description/)
```html
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
```
思路：头尾双指针， 碰头了返回 True，相同继续走，不同返回 False
```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return True
        head, tail = 0, len(s) - 1
        while head < tail:
            while not s[head].isalnum() and head < tail:
                head += 1
            while not s[tail].isalnum() and head < tail:
                tail -= 1
            if s[head].lower() != s[tail].lower():
                return False
            else:
                head += 1
                tail -= 1
        return True
```
总结：思路简单， 但是要想到的 case 很多。考虑带标点符号，连续两个位置都是标点符号，整个字符串都是标点符合这三个情况才能写对

### [1. Two Sum (Easy)](https://leetcode.com/problems/two-sum/description/)
```html

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
思路：固定一个找另一个
```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1 in xrange(len(nums)):
            for index2 in xrange(index1 + 1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]
```
总结： 第二层循环的起始数字注意条件 you may not use the same element twice

### [167. Two Sum II - Input array is sorted (Easy)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)
```html
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```
思路：

### [Lintcode 607. Two Sum III - Data structure design (Easy)](https://www.lintcode.com/problem/two-sum-iii-data-structure-design/description)
```html
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
add(1); add(3); add(5);
find(4) // return true
find(7) // return false

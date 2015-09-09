---
layout: post
title:  "Leetcode14 Longest Common Prefix"
date:   2015-09-08 00:00:00
categories: string
tags:
- String
---
原本发表在新浪微博上面：http://blog.sina.com.cn/s/blog_6f2e841a0102vvdy.html 既然刚弄了 jekyll， 就拷过来充个数。

很惭愧，少数几道自己独立思考写对的题。 刷题较郁闷， 就写一下思路放松一下吧。 听说 medium 以上的题大家也都看着答案刷的。

Google 搜出来这道题的第一个链接是 南郭子綦 的：http://www.cnblogs.com/zuoyuan/p/3779749.html ， 经常看他的答案。 还有一个经常搜到的是 http://yucoding.blogspot.com/ （墙内可能访问不了）， 他的 C++ 的答案全， Python 的据说正在加。 

开始说这道题吧。 题目如下：

Write a function to find the longest common prefix string amongst an array of strings.

我的思路是拿​ string 数组的第一个出来， 一个一个字母的和余下数组里面的 string 里的字母比对，如果余下数组里的 string 不含有或者不对的话就找到 longest common prefix string 了。 自认为比  南郭子綦 的代码清晰。 

如果能访问 github 的话， 代码在 https://github.com/alant/interview/blob/master/ex32_leet14_longest_common_prefix.py

不然的话代码如下：

{% highlight python linenos %}
# Write a function to find the longest common prefix string amongst an array of strings.

#tags: String

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if strs == []: return ""
        
        result = ""
        done = False
        for i in range(len(strs[0])):
            char = strs[0][i]

            for str in strs:
                if i > len(str) - 1:
                    done = True
                    break
                if char != str[i]:
                    done = True
                    break
            if done:
                break
            result += char
        return result

solution = Solution()
testInput = ["abc", "abcd", "abdd"]
print solution.longestCommonPrefix(testInput)
{% endhighlight %}

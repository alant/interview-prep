# Write a function to find the longest common prefix string amongst an array of strings.

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

class Solution(object):
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        先比较前两个字符串的最长公共前缀，之后用前缀依次与后面的字符串比较
        """
        if not strs:
            return ''
        if len(strs)==1:
            return strs[0]
        str1, str2 = strs[0], strs[1]
        res = ''
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                res += str1[i]
            else:
                break
        if not res:
            return res
        for j in range(2, len(strs)):
            if not strs[j]:
                return ''
            if len(res) <= len(strs[j]) and strs[j][:len(res)] == res:
                continue
            else:
                res = self.longestCommonPrefix1([res, strs[j]])
                if not res:
                    return res
        return res

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        通过zip(*list)可以将原打包的可迭代对向分开
        """
        if not strs:
            return ''
        for i, char_list in enumerate(zip(*strs)):
            if len(set(char_list)) > 1:
                return strs[0][:i]
        return min(strs)
t = Solution()
for i in [["dog","racecar","car"], ["flower","flow","flight"], ["abab","aba",""], ["ac","ac","a","a"]]:
    print(t.longestCommonPrefix(i))


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return
        tdict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90,
                 'CD':400, 'CM':900}
        res = 0
        flag = False
        for i in range(len(s)):
           if flag:
               flag=False
               continue
           if i < len(s)-1 and s[i:i+2] in tdict:
               res += tdict[s[i:i+2]]
               flag=True
           else:
               if s[i] not in tdict:
                   return
               res += tdict[s[i]]
               flag=False
        return res
t = Solution()
for i in ['III', 'IV', "LVIII", "MCMXCIV"]:
    print(t.romanToInt(i))




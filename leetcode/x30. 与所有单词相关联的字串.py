class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str] 其中每个word长度相同！！！
        :rtype: List[int]
        """
        if not s or not words:
            return []
        word_len = len(words[0])
        str_len = word_len * len(words)
        res = []
        times = {}
        # times记录words中单词的分布情况
        for i in words:
            if i not in times:
                times[i] = 0
            times[i] += 1
        # 从不同起点开始对单词进行分割，
        # 如"barfoothe" with k = 3, 从i=0开始分割可得["bar", "foo", "the"] 从i=1开始["arf", "oot"]，从i=2开始["rfo", "oth"]
        for i in range(word_len):
            self.findSubstring_core(i, s, res, word_len, str_len, times)
        return res
    def findSubstring_core(self, str_start, s, res, word_len, str_len, times):
        '''
        依照分布相同寻找与单词相关联的子串
        :param str_start:
        :param s:
        :param res:
        :param word_len:
        :param str_len:
        :param times:
        :return:
        '''
        word_start = str_start    # word_start记录s中字符串开始的位置，str_start记录当前遍历到的位置
        cur = {}
        while str_start + word_len <= len(s):
            word = s[str_start: str_start+word_len]
            str_start += word_len
            if word not in times:
                word_start = str_start
                cur.clear()
            else:
                if word not in cur:
                    cur[word] = 0
                cur[word] += 1
                while cur[word] > times[word]:    # 若word出现次数大于times中，则往后移动，直到次数等于times
                    cur[s[word_start: word_start+word_len]] -= 1
                    word_start += word_len
                if str_start - word_start == str_len:
                    res.append(word_start)
        return







t = Solution()
s = "bacfoofoobarthefoobarman"
words = ["foo","bar"]
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
# s = ""
# words = []
# s = "aaa"
# words = ['aa', 'aa']
# words1 = ['a', 'b', 'a']
print(t.findSubstring(s, words))
# a = ['1', '2', '3']
# print(t.getsubstring(words))


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lst=defaultdict(list)
        for word in strs:
            key=''.join(sorted(word))
            lst[key].append(word)
        return list(lst.values())
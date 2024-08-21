# https://leetcode.com/problems/count-items-matching-a-rule/submissions/1363208209/
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        dictRuleKey = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        for item in items:
            pos = dictRuleKey[ruleKey]
            if item[pos] == ruleValue:
                count += 1
        return count
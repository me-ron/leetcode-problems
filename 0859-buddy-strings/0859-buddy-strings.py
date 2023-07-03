class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            if len(s)==len(set(s)):
                return False 
            else:
                return True

        index1 = -1
        index2 = -1

        for i in range(len(s)):
            if s[i] != goal[i]:
                if index1 == -1:
                    index1 = i
                elif index2 == -1:
                    index2 = i
                else:
                    return False

        if index2 == -1:
            return False

        return s[index1] == goal[index2] and s[index2] == goal[index1]
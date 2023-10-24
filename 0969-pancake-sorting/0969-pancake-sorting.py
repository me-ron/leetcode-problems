class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        j = len(arr) - 1
        while j > 0:
            max_index = arr.index(max(arr[0:j+1]))
            if max_index != j:
                arr[:max_index+1] = arr[:max_index+1][::-1]
                ans.append(max_index+1)
                arr[:j+1] = arr[:j+1][::-1]
                ans.append(j+1)
            j -= 1
        return ans
        
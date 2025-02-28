from typing import Dict, List


class Solution:

    def create_dict_from_str(self, strr: str) -> Dict:

        alphabets = {}
        for x in strr:
            if x not in alphabets:
                alphabets[x] = 1
            else:
                alphabets[x] += 1

        return alphabets

    def create_unique_string_from_str(self, strr: str) -> str:
        return ''.join(sorted(list(strr)))


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = {}

        for strr in strs:
            unique_strr = self.create_unique_string_from_str(strr)

            if unique_strr not in anagram_groups:
                anagram_groups[unique_strr] = [strr]
            else:
                anagram_groups[unique_strr].append(strr)

        groupped_strr = []

        for group in anagram_groups:
            groupped_strr.append(anagram_groups[group])

        return groupped_strr

if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(solution.groupAnagrams([""]))
    print(solution.groupAnagrams(["a"]))

    # print(solution.create_unique_string_from_str("eat"))

    # test_dict = {
    #     't': 1,
    #     'e': 1,
    #     'a': 1,
    # }

    # assert solution.create_dict_from_str("eat") == test_dict

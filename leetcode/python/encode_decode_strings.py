from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_strs = []
        for i in range(len(strs)):

            if strs[i] == '':
                strs[i] = '*'

            encoded_chrs = []
            for c in strs[i]:
                encoded_chrs.append(f"{ord(c)}")

            encoded_strs.append("|".join(encoded_chrs))

        return "#".join(encoded_strs)


    def decode(self, s: str) -> List[str]:

        if len(s) == 0:
            return []

        encoded_strs = s.split("#")

        for i in range(len(encoded_strs)):
            if encoded_strs[i] == '42':
                encoded_strs[i] = ''

        for i in range(len(encoded_strs)):

            if encoded_strs[i] == '':
                continue

            decoded_chrs = []
            encoded_chrs = encoded_strs[i].split("|")

            for c in encoded_chrs:
                decoded_chrs.append(chr(int(c)))

            encoded_strs[i] = "".join(decoded_chrs)

        return encoded_strs


if __name__ == "__main__":

    solution = Solution()
    # print(solution.decode(solution.encode(["neet","code","love","you"])))
    # print(solution.decode(solution.encode([])))
    # print(solution.decode(solution.encode([""])))
    print(solution.decode(solution.encode(["we","say",":","yes","!@#$%^&*()"])))

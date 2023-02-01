class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len = len(str1)
        str2_len = len(str2)
        gcd = self.find_gcd(str1_len, str2_len)

        if str1[0: gcd] != str2[0: gcd]:
            return ''

        for div_len in range(gcd, 0, -1):
            if (
                    str1[0: div_len] * (str1_len // div_len) == str1
                    and str2[0: div_len] * (str2_len // div_len) == str2
            ):
                return str1[0: div_len]
        return ''

    def find_gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

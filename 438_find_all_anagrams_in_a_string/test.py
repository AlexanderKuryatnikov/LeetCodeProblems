from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        'cbaebabacd',
        'abc',
        [0, 6]
    ],
    '2: leetcode example 2': [
        'abab',
        'ab',
        [0, 1, 2]
    ],
    '3: anagram in the end of string': [
        'baaabb',
        'bab',
        [3]
    ],
    '4: second string is anagram': [
        'abcd',
        'bcda',
        [0]
    ],
    '5: same symbols with no anagram': [
        'baaaaabaaab',
        'abab',
        []
    ],
    '6: first string is shorter': [
        'abc',
        'abcd',
        []
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.findAnagrams(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')

from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        'ab',
        'eidbaooo',
        True
    ],
    '2: leetcode example 2': [
        'ab',
        'eidboaoo',
        False
    ],
    '3: permutation in the end of string': [
        'bab',
        'baaabb',
        True
    ],
    '4: second string is permutation': [
        'abcd',
        'bcda',
        True
    ],
    '5: same symbols with no permutation': [
        'abab',
        'baaaaabaaab',
        False
    ],
    '6: second string is shorter': [
        'abcd',
        'abc',
        False
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.checkInclusion(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')

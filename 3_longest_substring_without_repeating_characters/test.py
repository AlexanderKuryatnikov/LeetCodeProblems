from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: empty string': [
        '',
        0
    ],
    '2: one char': [
        'a',
        1
    ],
    '3: two same chars': [
        'aa',
        1
    ],
    '4: long string of same char': [
        'aaaaaaaaa',
        1
    ],
    '5: longest substring is string itself': [
        'abcdefg',
        7
    ],
    '6: longest substring first': [
        'ab1cde1f',
        6
    ],
    '7: longest substring last': [
        'a1b1cde',
        5
    ],
    '8: logest substring in the middle': [
        '1a1bcdefg1h1',
        8
    ],
    '9: substrings intersect with first longer': [
        'a1bc2de1f2g',
        7
    ],
    '10: substrings intersect with second longer': [
        'a1bc2d1efg2h',
        8
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.lengthOfLongestSubstring(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')

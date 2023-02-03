from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: one char': [
        'a',
        1
    ],
    '2: no spaces after last word': [
        'Hello World',
        5
    ],
    '3: spaces after last word': [
        '   fly me   to   the moon  ',
        4
    ],
    '4: one word surrounded by spaces': [
        '    awesome   ',
        7
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.lengthOfLastWord(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')

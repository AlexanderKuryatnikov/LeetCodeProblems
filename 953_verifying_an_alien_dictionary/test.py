from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: matching characters longer first': [
        ['apple', 'app'],
        'abcdefghijklmnopqrstuvwxyz',
        False
    ],
    '2: matching characters shorter first': [
        ['app', 'apple'],
        'abcdefghijklmnopqrstuvwxyz',
        True
    ],
    '3: correct order': [
        ['hello', 'leetcode'],
        'hlabcdefgijkmnopqrstuvwxyz',
        True
    ],
    '4: wrong order': [
        ['word', 'world', 'row'],
        'worldabcefghijkmnpqstuvxyz',
        False
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.isAlienSorted(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')

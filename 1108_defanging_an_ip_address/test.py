from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        '1.1.1.1',
        '1[.]1[.]1[.]1'
    ],
    '2: leetcode example 2': [
        '255.100.50.0',
        '255[.]100[.]50[.]0'
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.defangIPaddr(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')

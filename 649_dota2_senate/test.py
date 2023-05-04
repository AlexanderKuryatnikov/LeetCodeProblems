from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        'RD',
        'Radiant'
    ],
    '2: leetcode example 2': [
        'RDD',
        'Dire'
    ],
    '3: initiative with enough numbers': [
        'DDRRR',
        'Dire'
    ],
    '4: initiative with not enough numbers': [
        'DDRRRR',
        'Radiant'
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.predictPartyVictory(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')

from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        '25525511135',
        ['255.255.11.135',
         '255.255.111.35']
    ],
    '2: leetcode example 2': [
        '0000',
        ['0.0.0.0']
    ],
    '3: leetcode example 3': [
        '101023',
        ['1.0.10.23',
         '1.0.102.3',
         '10.1.0.23',
         '10.10.2.3',
         '101.0.2.3']
    ],
    '4: no valid ip 1': [
        '123',
        []
    ],
    '5: no valid ip 2': [
        '99999999999999999999',
        []
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.restoreIpAddresses(values[0])
        assert result == values[1], (
            f'Test {test}. Your result {result}'
        )
        print(f'Test {test}... OK')

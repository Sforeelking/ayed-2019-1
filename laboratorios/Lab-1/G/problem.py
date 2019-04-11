import json


# TODO Complete!
def solve(m, words):
    return m


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            m = test["m"]
            words = test["words"]
            actual = solve(m, words)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')

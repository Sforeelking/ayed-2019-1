import json

def solve(a,b):
    if a>0:
        b= b + text[a-1]
        return solve(a-1,b)
    else:
        return b
# TODO Complete!!
def reverse(text):
    a= len(text)-1
    b= text[a]
    return solve(a,b)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')

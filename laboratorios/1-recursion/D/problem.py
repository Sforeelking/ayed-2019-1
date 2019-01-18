import json

def solv(n) : 
    if (n == 1 or n == 0) : 
        return 1
    elif (n == 2) : 
        return 2
      
    else : 
        return solv(n - 3) + solv(n - 2) + solv(n - 1)  
# TODO Complete!
def compute_ways(n):
    return solv(n)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            actual = compute_ways(n)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | expected: {expected}, actual: {actual}'
        print('OK!')

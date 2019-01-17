import json
def solve0(p):
    if len(p)!=1:
        q= solve(p,1,int(p[0]))
        return solve0(q)
    else:
        return int(p)
def solve(lista,a,suma):
    if a< len(lista):
        return solve(lista,a+1,suma+ int(lista[a]))
    else:
        return str(suma)
# TODO Complete!
def super_digit(n, k):
    return solve0(n*k)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            k = test["k"]
            actual = super_digit(n, k)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | k: {k} | expected: {expected}, actual: {actual}'
        print('OK!')

import json
def sort(lista,a,par,imp):
    if a< len(lista):
        if lista[a]%2==0:
            par.append(lista[a])
        else:
            imp.append(lista[a])
        return sort(lista,a+1,par,imp)
    else:
        return par+imp
# TODO Complete!
def arrange(numbers):
    return sort(numbers,0,[],[])


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')

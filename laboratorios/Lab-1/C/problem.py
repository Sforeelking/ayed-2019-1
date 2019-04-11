import json

def solve(cont,lista,a,v,B):
    if a< len(lista):
        if  (lista[a] in v) or (lista[a] in B):
            cont+=1
        else:
            cont-=1
        return solve(cont,lista,a+1,v,B)
    else:
        if cont>0:
            return True
        else:
            return False
# TODO Complete!
def has_more_vowels(s):
    return solve(0,s,0,"aeiou","AEIOU")


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')

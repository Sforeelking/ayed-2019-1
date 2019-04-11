import json
def solv(disc, source,destination, aux):
    if disc>1:
        solv(disc-1,source,aux,destination)
    print(f"{source} → {destination}")
    if disc>1:
        solv(disc-1, aux, destination, source)
# TODO Complete!
def hanoi(n):
    return solv(n,"A","B","C")


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            hanoi(n)
        print('OK!')

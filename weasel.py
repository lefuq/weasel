from random import random, choices

target = 'METHINKS IT IS LIKE A WEASEL'
letters = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
parent = ''.join(choices(letters, k=28))


def accuracy(challenger):
    result = 0
    for i in range(len(challenger)):
        if challenger[i] == target[i]:
            result += 1
    return result


def generation(parent, branch):
    gen = {}
    c = 0
    while c < 100:
        child = ''
        for i in parent:
            if random() > 0.05:
                child += ''.join(i)
            else:
                child += ''.join(choices(letters, k=1)[0])
        c += 1
        gen[accuracy(child)] = child
    strongest_child = gen[max(gen)]
    if strongest_child == target:
        print(branch, strongest_child)
    else:
        print(branch, strongest_child)
        generation(strongest_child, branch+1)


generation(parent, 0)

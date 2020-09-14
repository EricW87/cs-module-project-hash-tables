"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
q = set(range(1, 200))
#q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
look_up = {}
perm_look_up = {}
#perm_look_up[3] = [[1], [3], [4], [7], [12]]

def calc(a, b, c, d):
    fa = 0
    fb = 0
    fc = 0
    fd = 0
    fabs = 0
    fcds = 0

    if a in look_up:
        fa = look_up[a]
    else:
        fa = f(a)
        look_up[a] = fa

    if b in look_up:
        fb = look_up[b]
    else:
        fb = f(b)
        look_up[b] = fb
    
    if c in look_up:
        fc = look_up[c]
    else:
        fc = f(c)
        look_up[a] = fc

    if d in look_up:
        fd = look_up[d]
    else:
        fd = f(d)
        look_up[d] = fd

    fabs = fa + fb
    fcds = fc - fd

    if(fabs == fcds):
        print(f'f({a}) + f({b}) = f({c}) - f({d})', end="    ")
        print(f'{fa} + {fb} = {fc} - {fd}')

#get all combos of a,b,c,d
def generatePermutations(q, a=[], max=4):
    #print(q, perm, a, max)
    if len(a) == max:
        #print(a)
        calc(a[0], a[1], a[2], a[3])
        return


    for e in q:
        a1 = a.copy()
        a1.append(e)
        generatePermutations(q, a1, max)


perm = generatePermutations(q)

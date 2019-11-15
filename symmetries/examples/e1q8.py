# check if y is cyclic permutation of x
def isPerm(x, y):
    for perm in cyclic_perms(x):
        if perm==y:
            return True
    return False


def cyclic_perms(array):
    for i in range(len(array)):
        yield(array)
        array.insert(0, array.pop())


# Kroenicker delta
def delta(a, b):
    if a==b:
        return 1
    else:
        return 0


# totally anti-symmetric tensor
def epsilon(a, b, c, d):
    if isPerm([a, b, c, d], [1, 2, 3, 4]):
        return 1
    elif isPerm([a, b, c, d], [2, 1, 3, 4]):
        return -1
    return 0

def isSame(i, l, q, p, j, m):
    left = delta(i, p) * delta(j, l) * delta(m, q)
    right = delta(l, p) * delta(m, i) * delta(j, q)
    d = left - right
    e = sum(epsilon(n, i, l, q) * epsilon(n, p, j, m) for n in range(0, 5))
    return d==e

def check_identity():
    for i in range(1, 5):
        for l in range(1, 5):
            for q in range(1, 5):
                for p in range(1, 5):
                    for j in range(1, 5):
                        for m in range(1, 5):
                            if not isSame(i, l, q, p, j, m):
                                print(i, l, q, p, j, m)


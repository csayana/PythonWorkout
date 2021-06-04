import itertools as it


'''     N Queens: Brute Force Solution Code     '''


def brute_force_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False

    return True


for perm in it.permutations(range(5)):
    if brute_force_solution(perm):
        print(perm)


'''     N Queens: Backtracking Solution Code        '''


def backtracking_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if backtracking_solution(perm):
                extend(perm, n)

            perm.pop()


extend(perm=[], n=20)

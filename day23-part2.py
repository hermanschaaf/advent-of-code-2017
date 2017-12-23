# h = 0
# b = 106500
# c = b + 17000

# # calculates total number of factors for nums in range
# for i in range(b, c, 17):
#     d = 2
#     found = False
#     while d < i:
#         e = 2
#         while e < i:
#             if d * e == i:
#                 found = True
#             e += 1

#         d += 1
#     if found:
#         h += 1

# print(h)


def factors(mx):
    """
    Calculate factors for all numbers from 1 to mx.
    Returns a list of sets, with the 0-index containing
    only set([0]).

    Time: O(N.logN)
    Space: O(N^2)
    """
    cnt = 0
    f = [set([1, i]) for i in range(0, mx + 1)]
    f[0] = set([0])
    for i in range(2, mx + 1):
        for u in range(2, i + 1):
            c = i * u
            if c > mx:
                break
            cnt += 1
            f[i * u].add(i)
            f[i * u].add(u)
    return f

if __name__ == '__main__':
    b = 106500
    c = 123500
    f = factors(c)
    h = 0
    for i in range(b, c + 1, 17):
        if len(f[i]) > 2:
            h += 1
    print(h)

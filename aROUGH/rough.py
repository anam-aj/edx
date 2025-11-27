n = 4

ls = [[False] * n] * n
print(ls)
print(type(ls))

ls2 = [[False] * n for _ in range(n)]
print(ls2)
print(type(ls2))

print(ls==ls2)

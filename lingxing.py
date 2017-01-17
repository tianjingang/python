s = '*'
for i in range(1,8,2):
    t = (7-i)//2
    print(' '*t + s*i + ' '*t)
for i in reversed(range(1,6,2)):
    t = (7-i)//2
    print(' '*t + s*i + ' '*t)

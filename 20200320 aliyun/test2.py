def check(d, start):
    i = ord('a')
    m = 0
    while i <= start:
        m = max(d[i], m)
        d[i] = m
        i += 1



start = ord('a')
dic = {}
for i in range(26):
    dic[start + i] = 0
num = int(input())
lst = []
for i in range(num):
    s = input()
    lst.append((ord(s[0]),ord(s[-1]), len(s)))
lst.sort(key = lambda x: x[0])
lst.sort(key = lambda x: x[1])


end = ord('a')
for i in range(len(lst)):
    check(dic, lst[i][1])
    dic[lst[i][1]] = max(dic[lst[i][0]] + lst[i][2], dic[lst[i][1]])

check(dic, ord('z'))
print(dic)
print(dic[ord('z')])
        


from fnmatch import *
f = open('17avarage.txt')
a = [int(x) for x in f]
res = []
fnn = 0
for i in range(len(a)):
        if fnmatch(str(a[i]),'?1?7'):
                fnn = max(fnn, a[i])
                   

for i in range(len(a)):
        for j in range(i+1, len(a)):
                if ((a[i]% 5 == 0 and a[j]% 7 == 0) + (a[i]% 7 == 0 and a[j]% 5 == 0))==1:
                        s = a[i]+a[j]
                        if s > fnn:
                                res.append(s)
                        
print(len(res), max(res))

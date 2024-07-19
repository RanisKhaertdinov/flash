f = open('17easy.txt')
a = [int(x) for x in f]
c = 0
res = []
for i in range(len(a)-3):
        if a[i]**3 + a[i+1]**3 == a[i+2]**3 + a[i+3]**3:
                s = a[i]+a[i+1]+a[i+2]+a[i+3]
                res.append(s)
print(len(res), max(res))

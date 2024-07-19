f = open('17hard.txt')
a = [int(x) for x in f]

res = []

fib = [1, 1]
for i in range(1, 20):
        fib.append(fib[i-1]+fib[i])
        
min8 = 10**10
for i in range(len(a)):
        if a[i] % 10 == 8:
                min8 = min(min8, a[i])

for i in range(len(a)-3):
        if ((a[i] in fib) + (a[i+1] in fib) + (a[i+2] in fib)) == 1:
                s = a[i] + a[i+1] + a[i+2]
                if s % min8 == 0:
                        res.append(s)
print(len(res), max(res))

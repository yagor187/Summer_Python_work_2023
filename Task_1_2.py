x, y = int(input("Enter your number-->")), int(input("Enter your number-->"))
s = []
s.append(x+y)
s.append(x-y)
s.append(x*y)
s.append(x/y)
s.append(x//y)
max = s[0]
for i in range(len(s)):
    if s[i] > max:
        max = s[i]
print(max)
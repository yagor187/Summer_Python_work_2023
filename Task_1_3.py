x, y = int(input("Enter your number-->")), int(input("Enter your number-->"))
s = []
s.append(x+y)
s.append(x-y)
s.append(x*y)
s.append(x/y)
s.append(x//y)
for i in range(len(s)):
    for j in range(len(s) - i - 1):
        if s[j] < s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]
print("Second largest number =", s[1])
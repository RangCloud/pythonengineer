k = ["불고기", "비빔밥"]
c = ["짜장", "짬뽕"]
a = [k, c]
print(k);
print(c);
print(a);

s = "Hello Python";
print("\n" + s[0], s[4])
print(s[-1], s[-4])
print(s[6:10])
print(s[-2:])
print(s[:5], s[6:])
print(s[::-1] + "\n")

b = []
b.append(1)
b.append([2, 3])
b.extend([4, 5])
b.insert(2, 0)
print(b)
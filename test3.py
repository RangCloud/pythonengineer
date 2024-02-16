s = []
s.extend("Hello Python")
s.remove("l")
print(s.index('P'))
print(s.pop(5))
print(s)
print("\n")

d = {"name": "파이썬", "age": 20}
d["sight"] = 1.5
d["age"] = 30
print(d)
print("\n")

a = 10
b = 20
if a > b:
    print("a가 큽니다.")
elif a == b:
    print("두 수가 같습니다.")
else:
    print("b가 큽니다.")
print("\n")

c = [10, 20, 30]
for i in c:
    print(i, end=" ")
print("\n")

for i in range(1,7,2):
    print(i, end=" ")
print()
for i in range(10):
    print(i, end=" ")
print()
for i in range(5,8):
    print(i, end=" ")
print()
for i in range(5,1,-1):
    print(i, end=" ")
print("\n")

sum = 0;
cnt = 1;
while True:
    sum += cnt
    if sum > 100:
        break;
    cnt += 1
print(cnt)
print()

def multi(num):
    num *= 2
    return num

a = int(input("정수 입력: "))
res = multi(a)
print(res)
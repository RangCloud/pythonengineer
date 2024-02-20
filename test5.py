# 정처기 20년 4회 5번
lol = [[1,2,3], [4,5], [6,7,8,9]]
print(lol[0]);
print(lol[2][1]);
for sub in lol:
    for item in sub:
        print(item, end = "");
    print();
print();

# 정처기 21년 1회 5번
class good:
    li = ["seoul", "kyeonggi", "incheon", "daejeon", "daegu", "busan"]
    
g = good();

str01 = "";

for i in g.li:
    str01 = str01 + i[0];
    
print(str01);
print();

# 정처기 21년 2회 7번
a = 100;
result = 0;
for i in range(1, 3):
    result = a >> i;
    result = result + 1;
print(result);
print();

# 정처기 22년 2회 13번
a = "REMEMBER NOVEMBER";
b = a[:3] + a[12:16];
c = "R and %s" % "STR";
print(b + c);
print();

# 정처기 22년 3회 9번
TestList = [1, 2, 3, 4, 5];
TestList = list(map(lambda num : num + 100, TestList))

print(TestList);
print();
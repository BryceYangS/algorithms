# 음계
da = input().replace(" ", "")
result = ""
print(da)
tmp = da[0]
for idx in range(1,len(da)):
    if tmp < da[idx]:
        if result == "descending":
            result = "mixed"
            break
        tmp = da[idx]
        result = "ascending"
    if tmp > da[idx]:
        if result == "ascending":
            result = "mixed"
            break
        tmp = da[idx]
        result = "descending"
print(result)



# 음계 풀이
a = list(map(int, input().split(" ")))
ascending = True
descending = True

for i in range(1,8):
    if a[i] < a[i - 1]:
        ascending = False
    elif a[i] > a[i - 1]:
        descending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")

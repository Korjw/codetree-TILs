temp = []
for _ in range(3):
    temp.append(str(input()))
temp.sort(key = lambda x : len(x))
print(len(temp[-1])-len(temp[0]))
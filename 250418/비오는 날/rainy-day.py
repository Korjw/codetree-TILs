n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)
temp = []
for i in range(n):
    temp.append([date[i].replace("-",""),date[i],day[i],weather[i]])
temp.sort()
for item in temp:
    if item[3] == "Rain":
        print(item[1],item[2],item[3])
        break

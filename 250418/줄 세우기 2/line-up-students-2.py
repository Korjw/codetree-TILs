n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]
students.sort(key = lambda x : (x[0],-x[1]))
for item in students:
    for s in item:
        print(s,end= ' ')
    print()
# Please write your code here.
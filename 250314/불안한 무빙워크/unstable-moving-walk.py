n, k = map(int,input().split())
temp_list = list(map(int,input().split()))
moving = [[],[]]
people = []

for i in range(n):
    moving[0].append(temp_list[i])

for i in range(n,2*n):
    moving[1].append(temp_list[i])
moving[1].reverse()

def move_moving():
    temp = moving[0][-1]
    for i in range(n-1,0,-1):
        moving[0][i] = moving[0][i-1]
    moving[0][0] = moving[1][0]
    
    for i in range(n-1):
        moving[1][i] = moving[1][i+1]
    moving[1][-1] = temp
    
    for i in range(len(people)):     
        people[i] += 1
        if people[i] == n-1:
            people.remove(n-1)



def people_moving():
    for i in range(len(people)-1,-1,-1):     
        if moving[0][people[i]+1] and people[i]+1 not in people:
            people[i] += 1
            moving[0][people[i]] -= 1   
        if people[i] == n-1:
            people.remove(n-1)

    if 0 not in people and moving[0][0]:
        people.insert(0,0)
        moving[0][0] -= 1   

def check():
    count = 0
    for i in range(2):
        for j in range(n):
            if moving[i][j] == 0:
                count += 1
    if count >= k:
        return True
    return False

for i in range(100000000):
    move_moving()
    people_moving()
    if check():
        print(i+1)
        break

# print(moving[0])
# print(moving[1])
# print(people)
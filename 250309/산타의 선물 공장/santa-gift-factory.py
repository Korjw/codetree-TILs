q = int(input())

remove_belt_list = []

for _ in range(q):
    temp_list = list(map(int,input().split()))
    if temp_list[0] == 100:
        n,m = temp_list[1], temp_list[2] # n 12, m 3
        count = 3
        belt = [[[-1,-1] for _ in range(n // m)] for __ in range(m)]
        for i in range(m):
            for j in range(n // m):
                belt[i][j][0] = temp_list[count]
                count += 1
        
        for i in range(m):
            for j in range(n // m):
                belt[i][j][1] = temp_list[count]
                count += 1
    
    elif temp_list[0] == 200:
        count = 0
        w_max = temp_list[1]
        for i in range(len(belt)):
            if not len(belt[i]):
                continue
            if belt[i][0][1] <= w_max:
                count += belt[i][0][1]
                del belt[i][0]
            else:
                belt[i].append(belt[i][0])
                del belt[i][0]
        print(count)
    
    elif temp_list[0] == 300:
        count = -1
        r_id = temp_list[1]
        for i in range(len(belt)):
            remove_list = []
            for j in range(len(belt[i])):
                if belt[i][j][0] == r_id:
                    count = r_id
                    remove_list.append([r_id, belt[i][j][1]])
            for item in remove_list:
                belt[i].remove(item)
        print(count)

    
    elif temp_list[0] == 400:  
        count = -1
        f_id = temp_list[1]
        for i in range(len(belt)):
            move_list = []
            last_idx = len(belt[i])
            for j in range(len(belt[i])):
                if belt[i][j][0] == f_id:
                    count = i+1
                    for k in range(j,len(belt[i])):
                        move_list.insert(0,belt[i][k][:])
            for item in move_list:
                belt[i].insert(0, item)
            for _ in range(last_idx,len(belt[i])):
                del belt[i][last_idx]
        print(count)
    
    elif temp_list[0] == 500:
        b_num = temp_list[1]
        if (b_num-1) in remove_belt_list:
            print(-1)
            continue
        else:
            remove_belt_list.append(b_num-1)
            select_idx = -1

            for i in range(len(belt)):
                idx = (b_num+i) % len(belt)
                if idx not in remove_belt_list:
                    select_idx = idx
                    break
            for item in belt[b_num-1]:
                belt[select_idx].append(item)
            
            belt_count = len(belt[b_num-1])
            for _ in range(belt_count):
                del belt[b_num-1][0]
            
            print(b_num)
        #print(belt)

#print(belt)
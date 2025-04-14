string = list(map(str,input()))

string[1] = "a"
string[-2] = "a"
for item in string:
    print(item,end = '')
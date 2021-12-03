import sys
a = sys.argv[1]
b = sys.argv[2]
with open(a) as input: 
    dict = {} 
    list = [x.split(":") for x in input.read().splitlines()]
for i in list: 
    dict[i[0]] = str(i[1])
c = b.split(",")
for j in c:
    try: 
        print(f"{j},University: {dict[j]}")
    except: 
        print(f"No record '{j}' was found") 
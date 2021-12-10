value_ = open("final_output.txt", "r")

for i in range(10):
    print(value_.readline())
    temp = value_.readline()
    for items in temp.split():
        print(items)


key_ = open("flair_custom_entity.txt","r")
value_ = open("final_output.txt", "r")
output_ = open("train_data2.txt", "w")

for i in range(226):
    key_temp = key_.readline()
    value_temp = value_.readline()
    #print("[\"" + key_temp.strip() + "\"," +value_temp.strip() + "],")
    output_.write("[\"" + key_temp.strip() + "\"," +value_temp.strip() + "],")

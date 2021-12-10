slotDictionary = {'PRODUCTNAME': ['Poco M2', 'Motorola Edge 20',   'Apple Iphone',  'Roadster',
                                  'Dolo',   'Cashew Nut',   'Headphones',   'Laptop',   'Cricket Bat',
                                  'Suitcase',   'Samsung Note ',   'Horlicks', 'badminton',
                                  'MRF', 'Ceat', 'Kookabura', 'Gym workout Kit',  '4K TV',   'Earphones',   'Redmi Note 9',
                                  'Boat', 'JBL', 'Infinty', 'Samsung M51', 'Samsung Note',  'Sunflower Oil', 'Football',   'Yonex racquet',
                                  'Travel bags',   'Tshirt',   'Realme PowerBank',   'DSLR Camera',
                                  'Realme Narzo 5G', 'Ashirvad Atta',   'Peanut Butter',   'Roasted Almond',
                                                                        'Bata Footwear', 'T-shirt', 'footwear', 'jeans', 'sweaters', 'shoes', 'Carromboard',    'Mobile Case',    'DTH', 'eGPU'],

                  'CITY': ['Trivandrum', 'Bangalore', 'Kochi', 'Kollam', 'Chennai', 'Pune', 'Mumbai', 'Kolkota', 'India', 'Delhi'],
                  'CATEGORY': ['Sports', 'Grocery', 'Mobile', 'Fashion', 'Electronics'],
                  'PRICING': ['Expensive', 'Cheap', 'Average', 'High cost', 'Price', 'cost', 'high'],
                  'NUMBEROFPRODUCTS': ['two pairs', 'items', 'of them'],
                  'TIME': ['a.m.', 'p.m.', 'morning', 'evening', 'tomorrow', 'afternoon', 'days', 'night']}

allSlots = ['productname', 'numberofproducts',
            'city', 'time', 'category', 'pricing', 'cost']

# print(slotDictionary['city'])

scentences = open("flair_custom_entity.txt", "r")
output_ = open("final_output.txt", "w")


for i in range(225):
    temp = scentences.readline()
    output_.write('[')
    for key in slotDictionary:
        for keys in slotDictionary[key]:
            print(len(keys))

            if keys.lower() in temp.lower():
                output_.write("(\"" + keys + "\",\"" + key + "\")")
                #i += 1
    output_.write("]\n")

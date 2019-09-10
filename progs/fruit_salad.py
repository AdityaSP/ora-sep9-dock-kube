dict_fruits={} 
while True: 
    fruit = (input('Enter fruit name , to exit enter -1:').upper()) 
    if fruit=='-1': 
        break 
    else: 
        print ('Your choice was ',fruit) 
        if fruit in dict_fruits: 
            print('Fruit exists and will increment')
            dict_fruits[fruit] = dict_fruits[fruit] + 1
        else: 
            print('Fruit needs to be registered') 
            dict_fruits.update({fruit:1}) 
 
print('Entire dictionary is :',dict_fruits)
# dictionary (key value pair {}), unordered, changeable, 


# datas = {}
# print(type(datas))


datas = {'nepal': 'kathmandu', 
         'india': 'new delhi', 
         'china': 'beijing'}
# print(f"Capital city of Nepal is {datas['nepal']}")

# datas['nepal'] = 'Ktm'
# print(f"Capital city of Nepal is {datas['nepal']}")
# datas['japan'] = 'tokyo'
# print(datas['japan'])
# datas.pop('nepal') #removes nepal 
# print(datas)

for key in datas:
    print(key)

for key in datas:
    print(f"The capital of {key} is {datas[key]}")


# car = {'brand': 'Toyota', 'model': 'Corolla', 'year': '2024'}
# car_model = car['model']
# print(car_model)
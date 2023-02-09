import json

data={}
data['people'] =[]
data['people'].append({'name':'Андрей','website':'ya.ru','from':'Moskow'})
data['people'].append({'name':'Игорь','website':'py.ru','from':'Rostov'})
data['people'].append({'name':'Алла','website':'by.ru','from':'Volgograd'})
print(data)

with open ('data.json','w') as file: # create
    json.dump(data,file) #record use json.dump

print(file) # dont work - need reading

with open ('data.json','r') as file:
    print(json.load(file)) #reading use json.load

with open ('data.json') as file: # выводим красиво по ключам
    data=json.load(file)
    for f in data['people']:
        print('Name: '+ f['name'])
        print('Website: '+ f['website'])
        print('From: '+ f['from'])
        print('') #что-бы разделить выводимые значения
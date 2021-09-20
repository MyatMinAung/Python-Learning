Person={}
while True :
    name=input('name :')
    age=int(input('age :'))
    Person[name]=age
    another=input('another y/n :')
    if(another=='y') :
        continue
    else :
        break
 
for (key,value) in Person.items() :
    print(f"{key} {value}")
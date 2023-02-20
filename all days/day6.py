dog=dict()
dog['name']='Dog'
dog['color']='Brown'
dog['breed']='German Sheperd'
dog['legs']=4
dog['age']=3
print(dog)
student={
    "First name":"Aayush",
    "Last name":"Gurung",
    "Gender":"Male",
    "age":"22",
    "marital status":"Single",
    "skills":{"programming","Coding"},
    "country":"Nepal",
    "city":"Kathmandu",
    "address":"Chabahil"
}
print(len(student))
print(type(student["skills"]))
lst=student["skills"]
lst.add('Running')
student["skills"].add("Oksay")
print(student["skills"])
student["skills"].remove('Running')
print(student["skills"])

keys=student.keys()
values=student.values()
print(keys,values)

tup=student.items()
print(tup)

student.pop('age')
print(student)

dic=[0]
count=0
print(str(student["skills"]))
# for x in student:
#     dic=x[count]
#     count+=1
# print(dic)
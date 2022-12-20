"""Day 1: 30 Days of python programming"""
first_name='A'
last_name='G'
full_name='Aayush'
country='Nepal'
city='Kathmandu'
age=22
year=2000
is_married=False
multiple1,multiple2,multiple3='aayush','okay','good'
print(multiple1,multiple2)
print('checking type\n')
print(first_name,'type is ',type(first_name))
print(type(age))
print(type(year))
print(float(age))
print(type(str(age)))
print([ord(c) for c in full_name])
print('Length of First Name',len(first_name))
first_name_len=len(first_name)
last_name_len=len(last_name)

if first_name_len == last_name_len:
    print(first_name_len,last_name_len,'Both length are equal')
else:
    print(first_name_len,last_name_len,'Length not equal')
num_one=25
num_two=4
total= num_one+num_two
diff= num_one-num_two
product= num_two*num_one
division=num_one/num_two
remainder=num_one/num_two
exp=num_one**num_two
floor_division=num_one//num_two
print(total,diff,product,division,remainder,exp,floor_division)

radius=30
pi=3.14
area_of_circle=pi*radius**2
circumference=2*pi*radius
print('Area of circle',area_of_circle,'\nCircumference of circle',circumference)
# radius_input=int(input('Enter Radius'))
# area=pi*radius_input**2
# circumference_c=2*pi*radius_input
# print('Area of circle',area,'\nCircumference of circle',circumference_c)
fname=input('Enter first name')
lname=input('Enter last name')
countr=input('Enter country')
ag=input('Enter age')
print('Your Details')
print('Firstname:',fname,'\nLast Name:',lname,'\nCountry:',countr,'\nAge:',ag)

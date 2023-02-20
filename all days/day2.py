# multiline_string='''I am a student
# and i live in kathmandu and i love it'''
# print(multiline_string)
# first_name='Aayush'
# last_name='Gurung'
# full_name=first_name+last_name
# print(full_name)
# print('I live in kathmandu\n')
# print('This is tab\t a')
# print('This is Back slash\\')
# print('This is Single quote\'')
# print('This is Double quote\"')
# print('Table of content')
# print('Days\tTopics\tExercises')
# print('Sunday\t5\t6')
# print('Sunday\t5\t6')
# print('Sunday\t5\t6')
# print('Sunday\t5\t6')
# print('Sunday\t5\t6')
# radius=10
# pi=3.14
# area=pi*radius**2
# formated='The area of a circle of radius {} is {:.600f}'.format(radius,area)
# print(formated)
# a=5
# b=8
# c=7.678
# print(f'{a} + {b} = {a+b}')
# print(f'{a} - {b} = {a-b}')
# print(f'{a} % {b} = {a %b}')
# print(f'{a} * {b} = {a*b}')
# print(f'{a} + {c} = {a + c}')
# reverse='Reverse string'
# print(f'Reverse string {reverse[::-1]}')
# 
# a='Thirty '
# b='Days '
# c='Of '
# d='Python'
# concat=a+b+c+d
# print(concat)
# capital='captilazie method implement'
# print(capital.upper())
# counts='Therey arey foury y'
# print(counts.count('y',0,6))
# web=['Html','css','javascript']
# result = ''.join(web)
# print(result[0:8])
# print(web[0:5])
# a='thirty days of python'
# print(a.strip('rty'))
# a='python change1 change2'
# print(a)
# print(a.replace('change1','replacement'))
# a='thirty days, of pythonf,f in, Nepal'
# print(a.split('f'))
# a='thirty days of python'
# print(a.title())
# print(a.capitalize())
# print(a.replace('days','months'))
# print(a.split('days'))
# print(a.count('y'))
company='Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:14])
print(company.find('oding'))
a=company.replace('Coding','Python')
print(a)
print(a.replace('Python For All','Python for Everyone'))
print(company.split(' '))
cname='Facebook Google Microsoft Apple IBM Oracle Amazon'
print(cname.split(','))
print(company[0])
print(company[-1])
print(company[10])

def abbr(a):
    a=a.split(' ')
    c=' '
    for x in range(len(a)):
        
        st=str(a[x])
        c=c+st[0]
    print(c)

abbr(company)
abbr(cname)
print(company.index('C'))
print(company.find('F'))
print(company.rfind('F'))
sent='You cannot end a sentence with because because because is a conjunction'
print(sent.index('because'))
print(sent.rfind('because'))
print(sent[31:54])

print(company.startswith('Coding'))
print(company.endswith('coding'))
com='  Coding For All  '
print(com.strip())
b='thirty_days_of_python'
print(b.isidentifier())
lst=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
jn=' # '.join(lst)
print(jn)
a='I am enjoying this challenge.'
b='I just wonder what is next.'
print(a,'\n',b)
print('Name\tAge\tCountry\tCity\nAayush\t22\tNepal\tKathmandu')
radius=10
area=3.14*radius**2
pnt='The area of a circle with radius {} is {:.5f} meters square'.format(radius,area)
print(pnt)

def stutter(word):
	return (2*(word[:2]+'... '))+word+'?'
print(stutter('incredible'))

def disc(price,discount):
    return (price*(100-discount)*0.01)
print(disc(1500,50))
def maxi(s1,s2):
    return (s1+s2)-1
print(maxi(8,10))

matrix1=[
    [0,1,1,0],
    [1,0,1,1],
    [0,1,0,1],
    [0,1,1,0]
    ]
node1=0
node2=2
def ajdacent(matrix,node1,node2):
    # if matrix[node1][node2]==1:
    #     return True
    # else:
    #     return False
    return True if matrix[node1][node2]==1 else False
       

print(ajdacent(matrix1,node1,node2))

age=20
def calc_age(age):
    if age > 0:
        days = age * 365
        return days
    else:
        return 'Age cannot be zero'
print(calc_age(age))

def fact(number):
    y=1
    if number >= 0:
        for x in range(number):        
            y*=x+1
            print(y)
    else:
        return 'Please Enter Number greater than zero'
    return y

print(fact(5))

def planet(planeta,weight,planetb):
    forces={
        "Mercury":3.7,
        "Venus":8.87,
        "Earth":9.81,
        "Mars":3.71,
        "Jupiter":24.79,
        "Saturn":10.44,
        "Uranus":8.69,
        "Neptune":11.15
    }
    return round(weight/forces[planeta]*forces[planetb],2)

print(planet('Earth',1,'Mars'))


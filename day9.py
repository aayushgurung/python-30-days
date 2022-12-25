def add(a,b):
    return a+b
print(add(5,6))

def area_of_circle(r):
    return 3.14*r**2
print(area_of_circle(5))

def add_all_number(*num):
    sum=0
    for i in num:
        print(type(i))
        if isinstance(i,int):
            sum=sum+i
        else:
            sum=sum
    return sum

print(add_all_number(1,1,1,1,1,'5'))

def convert(c):
    f=c*(9/5)+32
    return f
    
print(f'{convert(31):.1f}')

def check_season(month):
    season={
    "Autum":["September","October","November"],
    "Winter":["January","February"],
    "Spring":["March","April","May"],
    "Summer":["June","July","August"]
    }
    if month in season["Autum"]:
        return "It is Autum Season"
    elif month in season["Spring"]:
        return "It is Spring Season"
    elif month in season["Winter"]:
        return "It is Winter Season"
    else:
        return "It is Summer Season"

print(check_season('September'))

def calculate_slope(x1,x2,y1,y2):
    m=(y2-y1)/(x2-x1)
    return m

print(calculate_slope(x1=8,x2=3,y1=3,y2=5))

def reverse_list(lst):
    return lst[::-1]

print(reverse_list(['a','b','c','d']))

def capitalize(lst):
    lst_tst=[]
    for i in lst:
        lst_tst.append(i.capitalize())
    return lst_tst

print(capitalize(['aayush','gurung','capitalize first']))

def add_item(lst,item):
    lst.append(item)
    return lst
    
print(add_item(['potato','mango'],'meat'))

def remove_item(lst,item):
    lst.remove(item)
    return lst
print(remove_item(['potato','mango','milk','meat'],'meat'))

def is_empty(a):
    if a == '':
        return 'It is empty'
    else:
        return 'It is not empty'

def isset(lst):
    return len(lst)== len(set(lst))

print(isset([1,1,2,3,4]))



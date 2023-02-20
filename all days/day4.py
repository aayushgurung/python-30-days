emptytuple=()
print(emptytuple)
tpl = ('item1', 'item2', 'item3','item4')
print('item5' in tpl)

family=('sarah','saswat','anwesh','abishek')
brother=('abishek','anwesh')
sister=('sarah','mandira')
siblings=brother+sister

print(siblings)
print(len(siblings))
lst=list(siblings)
lst.insert(0,'Dharma')
lst.insert(1,'Devi')
print(lst)
family=tuple(lst)
print(family)

fruits=('banana','apple')
vegetables=('carrot','tomato','ok','oksdfksdj')
animal=('giraffe','lion')
food_studd_tp=fruits+vegetables+animal

print(food_studd_tp)

food_stuff_lt=list(food_studd_tp)

def middle(a):
    leng=len(a)//2
    if int(len(a))%2==0:
        print(a[leng],a[leng-1])
        
    else:
        print(a[leng])
print(food_stuff_lt)
middle(food_studd_tp)
middle(food_stuff_lt)
food_stuff_lt.sort()
print(food_stuff_lt[0:3])
print(food_stuff_lt[-4:-1])



def double_events(nums):
    new_list=list()
    for x in range(len(nums)):
        if nums[x]%2==0:
            new_list.append(nums[x]*2)
        else:
            new_list.append(nums[x])
    return new_list

print(double_events([1,2,3,4]))

del food_studd_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonis' in nordic_countries)
print('')
word=['car','dog','animal']
def replace(word):
    new_list=[]
    for x in word:
        newstring=''

        for y in x:
            if y in ['a', 'e', 'i', 'o', 'u']:
                newstring+='vowel'
                print(newstring)
            else:
                newstring += y
                print(newstring)
        new_list.append(newstring)
    return new_list

print(replace(word))
        
def analyze(num):
    even=0
    odd=0
    sum=0
    count=0
    for x in num:
        print(x)
        sum+=x
        if x % 2==0:
            print('even',x)
            even+=x
            print('even sum:',even)
        else:
            odd+=x
        count+=1
    print(count)
    print(len(num))
    average=sum/len(num)
    dic={'even':even,'odd':odd,'sum':sum,'average':average}
    print(dic)

print(analyze([1,2,3,4,5,6,7,8,9,10]))
print(analyze([-2, -4, -6, -8]))
def array_diff(a,b):
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    print (a)
array_diff([1,2,2],[2])

def binary(num):
    sum=0
    count=num
    print(num)
    while(count/2!=0):
        print('a',count)
        sum+=count%2
        print('sum',sum)
        count=int(count/2)
        print('after dividing',count)
    return sum
print('return value',binary(55))


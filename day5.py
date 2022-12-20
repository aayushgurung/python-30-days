# st={'item1','item2'}
# print(st)

# st.add('itemadded')
# print(st)

# st.update(['item1u','item2u','item3u'])
# print(st)

# st.remove('item1')

# print(st)

# st.pop()
# print(st)
# st.clear()
# print(st)
# del st

# lst=['item','item1','item2']
# print(lst)
# st = set(lst)
# print(st)

# st1={'items','items1','itesm2','inter'}
# st2={'seconditem','items1','inter'}
# st3=st1.union(st2)
# print(st3)

# print(st1.intersection(st2))

# print(st2.issubset(st1))
# print(st2.issuperset(st1))

# print(st2.difference(st1))
# print(st1.difference(st2))

# print(st1.isdisjoint(st2))

# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# A = {19, 22, 24, 20, 25, 26,30,40}
# B = {19, 22, 20, 25, 24, 28, 27}
# age = [22, 19, 24, 25, 26, 24, 25, 24]

# print(len(it_companies))
# it_companies.add('twitter')
# print(it_companies)
# print('twitter' in it_companies)
# it_companies.update('openai','lenovo','dell')
# print(it_companies)
# it_companies.remove('Facebook')

# # A.union(B)
# # print(A)

# AnB=A.intersection(B)
# BnA=B.intersection(A)
# print('Intersection of A n B',AnB)
# print('Intersection of B n A',BnA)

# a={5,6,7}
# b={8,9,0}
# print('discjoint a b',a.isdisjoint(b))
# print(A.issubset(B))
# print(A.isdisjoint(B))

# print(A.union(B))
# print(B.union(A))
# print(A.symmetric_difference(B))
# del A
# del B

# ages_set=set(age)
# print(len(age)>len(ages_set))

# st='I am a teacher and I love to inspire and teach people'
# # strreplace=str.replace(' ','')
# print()


# print(st)

def sum_dig_pow(a,b):
    lst=list()
    for x in range(b+1):
        count=0
        d=0
        for y in iter(str(x)):
            count+=1
            c=int(y)
            d=d+c**count
            
            print(f'x: {x} and square: {d} and count:{count}')
        if d == x:
            lst.append(d)
    print(lst)

sum_dig_pow(1,100)
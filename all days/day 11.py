language = 'Python'
x=1
lst = [i for i in language if x ==1]

print(lst)

tup= [{i:i} for i in range(11)]
print(tup)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

faltte= [y for x in list_of_lists for y in x]

print(faltte)

list_of_lists = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
faltte= [c for x in list_of_lists for y in x for c in y]

print(faltte)

a=2
b=3

sum=lambda a,b:a+b
print(sum(5,4))

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filter_ok=[x for x in numbers if x<=0]
print(filter_ok)

pattern = [(x, 1, x**2, x**3, x**4, x**5, x**6) for x in range(11)]
print(pattern)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattten=[[list(y)] for x in countries for y in x]

print(flattten)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

flatten1=[c for x in names for y in x for c in y]

print(flatten1)


slope=lambda x1,x2,y1,y2: (y2-y1)/(x2-x1)

print(slope(1.1,2,4,9))
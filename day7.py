# Get user input using input(“Enter your age: ”). If user is 18 or older, 
# give feedback: You are old enough to drive. If below 18 give feedback 
# to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

age=int(input("Enter age"))
if age>18:
    print("You are old enought to learn to dirve")
else:
    age=19-age
    print(f"You need {age} more years to learn to drive ")

my_age=22
your_age=int(input("Enter your age"))
if your_age>my_age:
    age=your_age-my_age
    print(f'You are {age} years older than me')
else:
    age=my_age-your_age
    print(f'You are {age} years younger than me')

month=input("Enter month to get season")
season={
    "Autum":["September","October","November"],
    "Winter":["January","February"],
    "Spring":["March","April","May"],
    "Summer":["June","July","August"]
}
if month in season["Autum"]:
    print("It is Autum Season")
elif month in season["Spring"]:
    print("It is Spring Season")
elif month in season["Winter"]:
    print("It is Winter Season")
else:
    print("It is Summer Season")

fruits=['banana','orange','mango','lemon']
enter_fruits=input("Enter fruit name")

if enter_fruits in fruits:
    print("Fruits name already exists in the list")
else:
    fruits.append(enter_fruits)
    print(f'List after adding {enter_fruits} name is : {fruits}')

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print('has skills')
    middle=len(person['skills'])//2
    print(person['skills'][middle])
if 'Python' in person['skills']:
    print("person has python skills as well")
if 'Javascript' and 'React' in person['skills']:
    print('ful')
import string
import random


random_user_id=''
for x in range(6):
    if random.randint(0,1)==1:
        random_user_id+=str(random.randint(0,9))
    else:
        random_user_id+=random.choice(list(string.ascii_lowercase))

print(random_user_id)

def user_id_gen_by_user():
    num_char=int(input('Enter number of character to be in user id'))
    num_id=int(input('Enter number of id to generate'))
    for y in range(num_id):
        random_user_id=''
        for x in range(num_char):
            if random.randint(0,2)==1:
                random_user_id+=str(random.randint(0,9))
            else:
                random_user_id+=random.choice(list(string.ascii_lowercase))
        print(random_user_id)    

# user_id_gen_by_user()

def rgb_color_gen():
    print(f'rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})')
rgb_color_gen()

def list_hexa_colors():
    rand_hex_color_list=list()
    for x in range(6):
        rand_hex_color='#'
        for y in range(6):
            rand_hex_color+=random.choice(list(string.hexdigits.replace('abcdef','')))
        rand_hex_color_list.append(rand_hex_color)
        
    print(rand_hex_color_list)


list_hexa_colors()

def list_rgb():
    rgb_list=list()
    for x in range(3):
        rgb_list.append(f'rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})')
    print(rgb_list)
list_rgb()

def generate_colors(color_scheme,num_of_color_to_generate):
    if color_scheme.lower() =='hexa':
        rand_hex_color_list=list()
        for x in range(num_of_color_to_generate):
            rand_hex_color='#'
            for y in range(6):
                rand_hex_color+=random.choice(list(string.hexdigits.replace('abcdef','')))
            rand_hex_color_list.append(rand_hex_color)
            
        print(rand_hex_color_list)
    elif color_scheme.lower() =='rgb':
        rgb_list=list()
        for x in range(num_of_color_to_generate):
            rgb_list.append(f'rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})')
        print(rgb_list)
    else:
        print('Entered scheme or number is wrong Enter again!')
        color_scheme=str(input('Enter scheme'))
        num_of_color_to_generate=int(input('Enter number of color to generate'))
        return(generate_colors(color_scheme,num_of_color_to_generate))

print('\nYour generated colors')
generate_colors('hexa',5)

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print(shuffle_list([1,2,3,4,5,6,7]))

def unique_random():
    random_list=list()
    while len(random_list)<7:
        number=random.randint(0,9)
        if number not in random_list:
            random_list.append(number)

    print(random_list)

unique_random()


lst=[2,4,3,5,6,7,1,8,9]
print(sorted(lst)==list(range(1,10)))
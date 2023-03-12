a=50000
Sum=0
final=list()
# for i in range(a):
#     ln=len(str(i))
#     digit=[int(x) for x in str(i)]
#     Sum= sum([digit[j]**ln for j in range(ln)])
#     if Sum == i:
#         final.append(Sum)
    

#     ln=0
#     digit=list()
#     Sum=0
# final = [sum([int(x)**len(str(i)) for x in str(i)]) for i in range(a) if sum([int(x)**len(str(i)) for x in str(i)]) == i]

final = [sum([int(x) ** len(str(i)) for x in str(i)]) for i in range(a) if sum([int(x)** len(str(i)) for x in str(i)])==i]


print(final)
    
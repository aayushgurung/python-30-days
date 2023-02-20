import itertools 
from collections import defaultdict

# dataset=[
#     ["A","B"],
#     ["B","C","A"],
#     ["A","C","D","E"],
#     ["A","B"],
#     ["B","C","E"],
#     ["A","B","C"],
# ]
dataset = [    ['apple', 'banana', 'orange', 'grapes'],
    ['apple', 'banana', 'grapes'],
    ['apple', 'banana'],
    ['apple', 'orange'],
    ['banana', 'orange', 'grapes']
]


min_support=2
lst=list()
frequent_items=defaultdict(int)

for i in dataset:
    for j in i:
        frequent_items[j]+=1

min_frequent_items=defaultdict(int) 

for i in frequent_items:
    if frequent_items[i]>=2:
        min_frequent_items[i]+=frequent_items[i]

item_sets=set(min_frequent_items.keys())


for i in range(2,len(dataset)):
    min_pair=defaultdict()
    temp=item_sets
    item_pairs=list(itertools.combinations(temp,i))


    pair_count=defaultdict(int)

    for i in item_pairs:
        for j in dataset:
            if set(i).issubset(set(j)):
                pair_count[i]+=1
    print(pair_count)
    temp_min_pair=defaultdict(int)

    for i in pair_count:
        if pair_count[i]>=1:
            temp_min_pair[i]+=pair_count[i]
        
    

    if len(temp_min_pair)==0:
        break
    min_pair=temp_min_pair

print(min_pair)


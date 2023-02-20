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
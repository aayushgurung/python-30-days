def strip_comments(strng, markers):
    lines=strng.split('\n')
    print(type(lines))
    for i,line in enumerate(lines):
        for j in markers:
            index=line.find(j)
            if index!=-1:
                lines[i]=lines[i][:index].rstrip()
    return '\n'.join(lines)

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))